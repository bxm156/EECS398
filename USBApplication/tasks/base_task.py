from lib.types import enum


class Task(object): 

    def __init__(self, listener):
        self.listener = listener
        self.result = None

    def get_result(self):
        return self.result
