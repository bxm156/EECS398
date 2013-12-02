import os
import csv
import numpy
import scipy.stats
import sqlite3
from threads.database_thread import DatabaseThread
from threads.serial_thread import SerialThread
from threads.realtime_thread import RealTimeThread
from tasks.sqlite.select_task import SQLiteSelectTask
from tasks.sqlite.select_data_task import SQLiteSelectDataTask
from tasks.sqlite.select_data_since_task import SQLiteSelectDataSinceTask
from tasks.sqlite.insert_task import SQLiteInsertTask
from pypreferences import PyPreferences
from realtime_store import RealTimeStore

import Queue

class WattrLib(object):

    db_queue = Queue.Queue()
    serial_queue = Queue.Queue()

    db_thread = None
    serial_thread = None

    preferences = None

    data_field_names = [
        'flags',
        'epoch',
        'voltage',
        'current',
        'period',
        'active_power',
        'reactive_power',
        'apparent_power',
        'phase_angle',
        'power_factor'
    ]

    realtime_store = RealTimeStore()
    realtime_thread = None
    realtime_listeners = 0

    def __init__(self):
        super(WattrLib, self).__init__()
        self.preferences = PyPreferences('wattr')

    def start_threads(self, serial_path, database_idle_func=None):
        assert 'db_path' in self.preferences
        assert serial_path
        self.db_thread = DatabaseThread(self.preferences['db_path'], self.db_queue, database_idle_func)
        self.db_thread.start()

        self.serial_thread = SerialThread(serial_path, self.serial_queue, self)
        self.serial_thread.start()

    def stop_threads(self):
        self.db_thread.join()
        self.serial_thread.join()

    def is_database_defined(self):
        if 'db_path' in self.preferences:
            return os.path.isfile(self.preferences['db_path'])

    def set_database_path(self, path):
        self.preferences['db_path'] = path

    def insert_data(self, tuple_list):
        task = SQLiteInsertTask()
        task.set_values(tuple_list)
        self.db_queue.put(task)

    def dump_data(self, start_time, end_time, path):
        
        def listener_function(task):
            results = [dict(row) for row in task.get_result()]
            with open(path, 'w+') as csv_file:
                writer = csv.DictWriter(csv_file, self.data_field_names)
                writer.writeheader()
                writer.writerows(results)

        task = SQLiteSelectTask(listener=listener_function)
        task.set_row_factory(sqlite3.Row)
        task.set_parameters({'start_time': start_time, 'end_time': end_time})
        self.db_queue.put(task)

    def get_data_stats(self, start_time, end_time, handler_function):
        def stat_func(task):
            rows = task.get_result()
            if not rows:
                return
            rows = numpy.asarray(rows)
            means = numpy.mean(rows, axis=0)
            medians = numpy.median(rows, axis=0)
            modes = scipy.stats.mode(rows, axis=0)[0][0]
            maximums = numpy.nanmax(rows, axis=0)
            minimums = numpy.nanmin(rows, axis=0)
            std = numpy.std(rows, axis=0)

            #Zips for histograms
            zipped = zip(*rows)
            voltages = zipped[0]
            currents = zipped[1]
            periods = zipped[2]
            active_powers = zipped[3]
            reactive_powers = zipped[4]
            apparent_powers = zipped[5]
            phase_angles = zipped[6]
            power_factors = zipped[7]

            handler_function(means, medians, modes, maximums, minimums, std,
                voltages=voltages,
                currents=currents,
                periods=periods,
                active_powers=active_powers,
                reactive_powers=reactive_powers,
                apparent_powers=apparent_powers,
                phase_angles=phase_angles,
                power_factors=power_factors
           )
            
        task = SQLiteSelectDataTask(listener=stat_func)
        parameters = {
            'start_time': start_time,
            'end_time': end_time,
        }
        task.set_parameters(parameters)
        self.db_queue.put(task)

    def get_realtime_store(self):
        return self.realtime_store

    def start_realtime_collection(self):
        self.should_collect_realtime = True
        self.realtime_listeners += 1
        if not self.realtime_thread:
            self.realtime_thread = RealTimeThread(self)
            self.realtime_thread.start()
    def stop_realtime_collection(self):
        self.realtime_listeners -= 1
        if self.realtime_listeners <= 0:
            self._stop_realtime_collection()
            self.realtime_thread = None

    def _stop_realtime_collection(self):
        self.realtime_thread.join()
        self.realtime_store.clear()

    def get_realtime_data(self, since, listener_func):
        task = SQLiteSelectDataSinceTask(listener=listener_func)
        task.set_parameters({'since_time': since})
        self.db_queue.put(task)

