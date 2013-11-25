import os
import csv
import numpy
import sqlite3
from threads.database_thread import DatabaseThread
from threads.serial_thread import SerialThread
from tasks.sqlite.select_task import SQLiteSelectTask
from tasks.sqlite.select_data_task import SQLiteSelectDataTask
from tasks.sqlite.insert_task import SQLiteInsertTask
from pypreferences import PyPreferences

import Queue

class WattrLib(object):

    db_queue = Queue.Queue()
    serial_queue = Queue.Queue()

    db_thread = None
    serial_thread = None

    preferences = None

    data_field_names = [
        'id',
        'device_id',
        'timestamp',
        'voltage',
        'current',
        'power',
        'spike',
        'dip',
        'failure'
    ]

    def __init__(self):
        super(WattrLib, self).__init__()
        self.preferences = PyPreferences('wattr')

    def start_threads(self, serial_path):
        assert 'db_path' in self.preferences
        assert serial_path
        self.db_thread = DatabaseThread(self.preferences['db_path'], self.db_queue)
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
                handler_function(None, None, None, None, None)
                return
            rows = numpy.asarray(rows)
            means = numpy.mean(rows, axis=0)
            medians = numpy.median(rows, axis=0)
            maximums = numpy.nanmax(rows, axis=0)
            minimums = numpy.nanmin(rows, axis=0)
            std = numpy.std(rows, axis=0)

            #Zips for histograms
            zipped = zip(*rows)
            voltages = zipped[0]
            currents = zipped[1]
            power = zipped[2]
            freq = zipped[3]

            handler_function(means, medians, maximums, minimums, std, voltages, currents, power, freq)
            
        task = SQLiteSelectDataTask(listener=stat_func)
        parameters = {
            'start_time': start_time,
            'end_time': end_time,
        }
        task.set_parameters(parameters)
        self.db_queue.put(task)
