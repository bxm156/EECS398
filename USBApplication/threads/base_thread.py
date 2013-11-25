import threading
import time


class BaseThread(threading.Thread):

    def __init__(self):
        super(BaseThread, self).__init__()
        self.should_terminate = threading.Event()
 
    def setup(self):
        pass

    def cleanup(self):
        pass

    def join(self, timeout=None):
        self.should_terminate.set()
        super(BaseThread, self).join(timeout)

    def loop(self):
        pass

    def run(self):
        self.setup()
        while not self.should_terminate.is_set():
            self.loop()
        # Cleanup
        self.cleanup()
