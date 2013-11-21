import wx

from ui.WattrMainFrame import WattrMainFrame
from controllers.graph_controller import GraphController
from controllers.device_selector_controller import DeviceSelectorController
from controllers.database_controller import DatabaseController
from lib.wattrlib import WattrLib
from lib.lib import wx_datetime_to_python_datetime
from lib.lib import fill_wx_date_with_time

class MainController(object):

    wattrlib = None

    def __init__(self, app):
        super(MainController, self).__init__()
        self.wattrlib = WattrLib()
        self.app = app
        self.app.m_frame = WattrMainFrame(None)
        self.app.m_frame.Show()
        self.app.m_frame.stats_dump_raw_data.Bind(wx.EVT_BUTTON, self.on_dump_data)

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


    def on_dump_data(self, evt):
        # Get StartTime
        start_date = self.app.m_frame.start_date_picker.GetValue()
        start_time = self.app.m_frame.start_time_picker.GetValue(as_wxDateTime=True)
        combined = fill_wx_date_with_time(start_date, start_time)
        start_datetime = wx_datetime_to_python_datetime(combined)

        # Get EndTime
        end_date = self.app.m_frame.end_date_picker.GetValue()
        end_time = self.app.m_frame.end_time_picker.GetValue(as_wxDateTime=True)
        combined = fill_wx_date_with_time(end_date, end_time)
        end_datetime = wx_datetime_to_python_datetime(combined)

        createFileDialog = wx.FileDialog(self.app.m_frame, "Save", "", "",
                                                        "CSV files (*.csv)|*.csv",
                                                        wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if createFileDialog.ShowModal() != wx.ID_CANCEL:
            path = createFileDialog.GetPath()
            self.wattrlib.dump_data(start_datetime, end_datetime, path)
        createFileDialog.EndModal(0)

    def exit(self):
        self.app.Exit()

    def on_exit(self):
        self.wattrlib.stop_threads()
