import os
import csv

from threads.database_thread import DatabaseThread

from tasks.sqlite.select_task import SQLiteSelectTask
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

    def start_threads(self):
        assert 'db_path' in self.preferences
        self.db_thread = DatabaseThread(self.preferences['db_path'], self.db_queue)
        self.db_thread.start()

    def stop_threads(self):
        self.db_thread.join()

    def is_database_defined(self):
        if 'db_path' in self.preferences:
            return os.path.isfile(self.preferences['db_path'])

    def set_database_path(self, path):
        self.preferences['db_path'] = path

    def dump_data(self, start_time, end_time, path):
        
        def listener_function(task):
            results = [dict(row) for row in task.get_result()]
            with open(path, 'w+') as csv_file:
                writer = csv.DictWriter(csv_file, self.data_field_names)
                writer.writeheader()
                writer.writerows(results)

        task = SQLiteSelectTask(listener=listener_function)
        task.set_parameters({'start_time': start_time, 'end_time': end_time})
        self.db_queue.put(task)
