from lib.types import enum


class BaseTask(object): 

    def __init__(self, listener=None):
        super(BaseTask, self).__init__()
        self.listener = listener
        self.result = None

    def run(self):
        raise NotImplementedError

    def cleanup(self):
        pass

    def get_result(self):
        return self.result
