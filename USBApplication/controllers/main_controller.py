from ui.WattrMainFrame import WattrMainFrame
from controllers.graph_controller import GraphController
from controllers.device_selector_controller import DeviceSelectorController
from controllers.database_controller import DatabaseController
from lib.wattrlib import WattrLib

class MainController(object):

    wattrlib = None

    def __init__(self, app):
        super(MainController, self).__init__()
        self.wattrlib = WattrLib()
        self.app = app
        self.app.m_frame = WattrMainFrame(None)
        self.app.m_frame.Show()

        #Database Selection
        if not self.wattrlib.is_database_defined():
            database_controller = DatabaseController(app.m_frame, self)
            database_controller.get_view().ShowModal()

        #Device Selection
        device_selector = DeviceSelectorController(app.m_frame.m_panel4, self)
        device_selector.get_view().ShowModal()

        app.SetTopWindow(app.m_frame)

        # Setup Graph for testing atm
        graph_controller = GraphController(app.m_frame.m_panel4)
        app.m_frame.m_panel4 = graph_controller.get_view()
        graph_controller.graph()

        # Start threads
        self.wattrlib.start_threads()

    def on_device_selected(self, com_string):
        pass

    def on_database_selected(self, db_path):
        self.wattrlib.set_database_path(db_path)

    def exit(self):
        self.app.Exit()

    def on_exit(self):
        self.wattrlib.stop_threads()
