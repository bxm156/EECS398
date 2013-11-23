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

        # Bind Buttons
        self.app.m_frame.stats_dump_raw_data.Bind(wx.EVT_BUTTON, self.on_dump_data)
        self.app.m_frame.stats_update_button.Bind(wx.EVT_BUTTON, self.on_update_stats)
        self.app.m_frame.disconnect_button.Bind(wx.EVT_BUTTON, self.on_disconnect)

        #Database Selection
        if not self.wattrlib.is_database_defined():
            database_controller = DatabaseController(app.m_frame, self)
            database_controller.get_view().ShowModal()

        #Device Selection
        self.show_device_selector()

        app.SetTopWindow(app.m_frame)

        # Setup Graph for testing atm
        graph_controller = GraphController(app.m_frame.m_panel4)
        app.m_frame.m_panel4 = graph_controller.get_view()
        graph_controller.graph()

    def show_device_selector(self):
        #Device Selection
        device_selector = DeviceSelectorController(self.app.m_frame.m_panel4, self)
        device_selector.get_view().ShowModal()

    def on_disconnect(self, evt):
        self.wattrlib.stop_threads()
        self.app.m_frame.device_conn_status.SetLabel("Disconnected")
        self.show_device_selector()

    def on_device_selected(self, com_string):
        # Start threads
        self.wattrlib.start_threads()

    def on_database_selected(self, db_path):
        self.wattrlib.set_database_path(db_path)

    def get_stats_times(self):
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
        return start_datetime, end_datetime

    def on_update_stats(self, evt):
        start_datetime, end_datetime = self.get_stats_times()
        
        def on_stats_update_ui(means, medians, maximums, minimums, std):
            if means is None:
                print "Failed"
                return

            # Mean
            self.app.m_frame.voltage_mean.SetLabel(str(means[0]) + " V")
            self.app.m_frame.current_mean.SetLabel(str(means[1]) + " A")
            self.app.m_frame.power_mean.SetLabel(str(means[2]) + " W")
            self.app.m_frame.freq_mean.SetLabel(str(means[3]) + " Hz")
            
            # Median
            self.app.m_frame.voltage_median.SetLabel(str(medians[0]) + " V")
            self.app.m_frame.current_median.SetLabel(str(medians[1]) + " A")
            self.app.m_frame.power_median.SetLabel(str(medians[2]) + " W")
            self.app.m_frame.freq_median.SetLabel(str(medians[3]) + " Hz")

            # Max
            self.app.m_frame.voltage_max.SetLabel(str(maximums[0]) + " V")
            self.app.m_frame.current_max.SetLabel(str(maximums[1]) + " A")
            self.app.m_frame.power_max.SetLabel(str(maximums[2]) + " W")
            self.app.m_frame.freq_max.SetLabel(str(maximums[3]) + " Hz")

            # Min
            self.app.m_frame.voltage_min.SetLabel(str(minimums[0]) + " V")
            self.app.m_frame.current_min.SetLabel(str(minimums[1]) + " A")
            self.app.m_frame.power_min.SetLabel(str(minimums[2]) + " W")
            self.app.m_frame.freq_min.SetLabel(str(minimums[3]) + " Hz")

            # STD
            self.app.m_frame.voltage_std.SetLabel(str(std[0]) + " V")
            self.app.m_frame.current_std.SetLabel(str(std[1]) + " A")
            self.app.m_frame.power_std.SetLabel(str(std[2]) + " W")
            self.app.m_frame.freq_std.SetLabel(str(std[3]) + " Hz")

        self.wattrlib.get_data_stats(start_datetime, end_datetime, on_stats_update_ui) 

    def on_dump_data(self, evt):
        start_datetime, end_datetime = self.get_stats_times()    
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
