import sqlite3
from datetime import datetime
from base_task import BaseTask


class SQLiteTask(BaseTask):

    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
    parameters = None
    row_factory = None

    def set_row_factory(self, factory):
        row_factory = factory

    def set_parameters(self, param_dict):
        for key, value in param_dict.items():
            if isinstance(value, datetime):
                param_dict[key] = value.strftime(self.TIMESTAMP_FORMAT) 
        self.parameters = param_dict

    def run(self, connection):
        connection.row_factory = self.row_factory

    def cleanup(self):
        pass
