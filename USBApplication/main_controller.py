from ui.WattrMainFrame import WattrMainFrame
from graph_controller import GraphController
from threads.database_thread import DatabaseThread
import Queue
from pypreferences import PyPreferences

class MainController(object):

    preferences = None

    def __init__(self, app):
        super(MainController, self).__init__()
        self.preferences = PyPreferences('wattr')
        app.m_frame = WattrMainFrame(None)
        app.m_frame.Show()
        app.SetTopWindow(app.m_frame)

        # Setup Graph for testing atm
        graph_controller = GraphController(app.m_frame.m_panel4)
        app.m_frame.m_panel4 = graph_controller.get_view()
        graph_controller.graph()

        # Start threads
        self.db_thread = DatabaseThread("test", Queue.Queue())
        self.db_thread.start()

    def on_exit(self):
        self.db_thread.join()
