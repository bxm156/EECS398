import sqlite3

from base_task import BaseTask


class SQLiteTask(BaseTask):

    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
    
    def set_parameters(self, param_dict):
        for key, value in param_dict.items():
            if isinstance(value, datetime):
                param_dict[key] = value.strftime(self.TIMESTAMP_FORMAT) 
        self.parameters = param_dict

    def set_parameters(self):
        raise NotImplementedError

    def run(self, connection):
        raise NotImplementedError

    def cleanup(self):
        pass
