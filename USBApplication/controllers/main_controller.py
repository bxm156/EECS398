import wx
import datetime
from ui.WattrMainFrame import WattrMainFrame
from controllers.graph_controller import GraphController
from controllers.device_selector_controller import DeviceSelectorController
from controllers.database_controller import DatabaseController
from controllers.histogram_controller import HistogramController
from controllers.animated_graph_controller import AnimatedGraphController
from tasks.sqlite.select_latest_data_task import SQLiteSelectLatestDataTask
from lib.wattrlib import WattrLib
from lib.lib import wx_datetime_to_python_datetime
from lib.lib import fill_wx_date_with_time


class MainController(object):

    wattrlib = None
    v_hist = []
    c_hist = []
    p_hist = []
    pf_hist = []
    f_hist = []

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
        self.app.m_frame.Bind(wx.EVT_CLOSE, self.on_exit)

        # Histogram buttons
        self.app.m_frame.voltage_histogram.Bind(wx.EVT_BUTTON, self.on_voltage_histogram)
        self.app.m_frame.current_histogram.Bind(wx.EVT_BUTTON, self.on_current_histogram)
        self.app.m_frame.period_histogram.Bind(wx.EVT_BUTTON, self.on_period_histogram)
        self.app.m_frame.active_power_histogram.Bind(wx.EVT_BUTTON, self.on_active_power_histogram)
        self.app.m_frame.reactive_power_histogram.Bind(wx.EVT_BUTTON, self.on_reactive_power_histogram)
        self.app.m_frame.apparent_power_histogram.Bind(wx.EVT_BUTTON, self.on_apparent_power_histogram)
        self.app.m_frame.phase_angle_histogram.Bind(wx.EVT_BUTTON, self.on_phase_angle_histogram)
        self.app.m_frame.power_factor_histogram.Bind(wx.EVT_BUTTON, self.on_power_factor_histogram)

        # Graph buttons
        self.app.m_frame.graph_voltage.Bind(wx.EVT_BUTTON, self.on_graph_voltage)

        #Database Selection
        if not self.wattrlib.is_database_defined():
            database_controller = DatabaseController(app.m_frame, self)
            database_controller.get_view().ShowModal()

        #Device Selection
        self.show_device_selector()

        app.SetTopWindow(self.app.m_frame)

        # Setup Graph for testing atm
        #graph_controller = GraphController(app.m_frame.m_panel4)
        #app.m_frame.m_panel4 = graph_controller.get_view()
        #graph_controller.graph()

    def on_voltage_histogram(self, evt):
        self.show_histogram(self.voltage_hist, "Frequency of Voltage", "Occurances", "Voltage (V)")

    def on_current_histogram(self, evt):
        self.show_histogram(self.current_hist, "Frequency of Current", "Occurances", "Current (A)")

    def on_period_histogram(self, evt):
        self.show_histogram(self.period_hist, "Frequency of Period", "Occurances", "Period")
 
    def on_active_power_histogram(self, evt):
        self.show_histogram(self.active_power_hist, "Frequency of Active Power", "Occurances", "Active Power, (W)")

    def on_reactive_power_histogram(self, evt):
        self.show_histogram(self.reactive_power_hist, "Frequency of Reactive Power", "Occurances", "Reactive Power, (VAR)")

    def on_apparent_power_histogram(self, evt):
        self.show_histogram(self.apparent_power_hist, "Frequency of Apparent Power", "Occurances", "Apparent Power, (VA)")

    def on_phase_angle_histogram(self, evt):
        self.show_histogram(self.phase_angle_hist, "Frequency of Phase Angle", "Occurances", "Phase Angle")

    def on_power_factor_histogram(self, evt):
        self.show_histogram(self.power_factor_hist, "Frequency of Power Factor", "Occurances", "Power Factor")


    def show_histogram(self, data, title, y, x):
        hc = HistogramController(self.app.m_frame)
        hc.plot_hist(data, title, x, y)
        hc.get_view().ShowModal()

    def on_graph_voltage(self, evt):
        vg = AnimatedGraphController(self.app.m_frame, self.wattrlib)
        vg.get_view().Show()

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
        self.wattrlib.start_threads(com_string, SQLiteSelectLatestDataTask(listener=self.on_update_ui))

    def on_update_ui(self, task):
        results = task.get_result()
        if len(results) != 1:
            return
        result = results[0]
        try:
            datetimestr = datetime.datetime.fromtimestamp(result[1]).strftime('%Y-%m-%d %H:%M:%S')
            self.app.m_frame.device_latest_time.SetLabel(datetimestr)
            self.app.m_frame.device_latest_voltage.SetLabel(str(result[2]) + " V")
            self.app.m_frame.device_latest_current.SetLabel(str(result[3]) + " A")
            self.app.m_frame.device_latest_period.SetLabel(str(result[4]))
            self.app.m_frame.device_latest_active_power.SetLabel(str(result[5]) + " W")
            self.app.m_frame.device_latest_reactive_power.SetLabel(str(result[6]) + " VAR")
            self.app.m_frame.device_latest_apparent_power.SetLabel(str(result[7]) + " VA")
            self.app.m_frame.device_latest_phase_angle.SetLabel(str(result[8]))
            self.app.m_frame.device_latest_power_factor.SetLabel(str(result[9]))
        except wx.PyDeadObjectError:
            pass

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
        
        def on_stats_update_ui(means, medians, modes, maximums, minimums, std, **kwargs):
            voltages = kwargs.get('voltages', [])
            currents = kwargs.get('currents', [])
            periods = kwargs.get('periods', [])
            active_powers = kwargs.get('active_powers', [])
            reactive_powers = kwargs.get('reactive_powers', [])
            apparent_powers = kwargs.get('apparent_powers', [])
            phase_angles = kwargs.get('phase_angles', [])
            power_factors = kwargs.get('power_factors', [])

            self.voltage_hist = voltages
            self.current_hist = currents 
            self.period_hist = periods
            self.active_power_hist = active_powers
            self.reactive_power_hist = reactive_powers
            self.apparent_power_hist = apparent_powers
            self.phase_angle_hist = phase_angles
            self.power_factor_hist = power_factors

            round_func = lambda x: round(x, 2)
            means = map(round_func, means)
            medians = map(round_func, medians)
            modes = map(round_func, modes)
            maximums = map(round_func, maximums)
            minimums = map(round_func, minimums)
            std = map(round_func, std)

            # Mean
            self.app.m_frame.voltage_mean.SetLabel(str(means[0]) + " V")
            self.app.m_frame.current_mean.SetLabel(str(means[1]) + " A")
            self.app.m_frame.period_mean.SetLabel(str(means[2]))
            self.app.m_frame.active_power_mean.SetLabel(str(means[3]) + " W")
            self.app.m_frame.reactive_power_mean.SetLabel(str(means[4]) + " VAR")
            self.app.m_frame.apparent_power_mean.SetLabel(str(means[5]) + " VA")
            self.app.m_frame.phase_angle_mean.SetLabel(str(means[6]))
            self.app.m_frame.power_factor_mean.SetLabel(str(means[7]))

            
            # Median
            self.app.m_frame.voltage_median.SetLabel(str(medians[0]) + " V")
            self.app.m_frame.current_median.SetLabel(str(medians[1]) + " A")
            self.app.m_frame.period_median.SetLabel(str(medians[2]))
            self.app.m_frame.active_power_median.SetLabel(str(medians[3]) + " W")
            self.app.m_frame.reactive_power_median.SetLabel(str(medians[4]) + " VAR")
            self.app.m_frame.apparent_power_median.SetLabel(str(medians[5]) + " VA")
            self.app.m_frame.phase_angle_median.SetLabel(str(medians[6]))
            self.app.m_frame.power_factor_median.SetLabel(str(medians[7]))

            # Mode
            self.app.m_frame.voltage_mode.SetLabel(str(modes[0]) + " V")
            self.app.m_frame.current_mode.SetLabel(str(modes[1]) + " A")
            self.app.m_frame.period_mode.SetLabel(str(modes[2]))
            self.app.m_frame.active_power_mode.SetLabel(str(modes[3]) + " W")
            self.app.m_frame.reactive_power_mode.SetLabel(str(modes[4]) + " VAR")
            self.app.m_frame.apparent_power_mode.SetLabel(str(modes[5]) + " VA")
            self.app.m_frame.phase_angle_mode.SetLabel(str(modes[6]))
            self.app.m_frame.power_factor_mode.SetLabel(str(modes[7]))

            # Max
            self.app.m_frame.voltage_max.SetLabel(str(maximums[0]) + " V")
            self.app.m_frame.current_max.SetLabel(str(maximums[1]) + " A")
            self.app.m_frame.period_max.SetLabel(str(maximums[2]))
            self.app.m_frame.active_power_max.SetLabel(str(maximums[3]) + " W")
            self.app.m_frame.reactive_power_max.SetLabel(str(maximums[4]) + " VAR")
            self.app.m_frame.apparent_power_max.SetLabel(str(maximums[5]) + " VA")
            self.app.m_frame.phase_angle_max.SetLabel(str(maximums[6]))
            self.app.m_frame.power_factor_max.SetLabel(str(maximums[7]))

            # Min
            self.app.m_frame.voltage_min.SetLabel(str(minimums[0]) + " V")
            self.app.m_frame.current_min.SetLabel(str(minimums[1]) + " A")
            self.app.m_frame.period_min.SetLabel(str(minimums[2]))
            self.app.m_frame.active_power_min.SetLabel(str(minimums[3]) + " W")
            self.app.m_frame.reactive_power_min.SetLabel(str(minimums[4]) + " VAR")
            self.app.m_frame.apparent_power_min.SetLabel(str(minimums[5]) + " VA")
            self.app.m_frame.phase_angle_min.SetLabel(str(minimums[6]))
            self.app.m_frame.power_factor_min.SetLabel(str(minimums[7]))

            # STD
            self.app.m_frame.voltage_std.SetLabel(str(std[0]) + " V")
            self.app.m_frame.current_std.SetLabel(str(std[1]) + " A")
            self.app.m_frame.period_std.SetLabel(str(std[2]))
            self.app.m_frame.active_power_std.SetLabel(str(std[3]) + " W")
            self.app.m_frame.reactive_power_std.SetLabel(str(std[4]) + " VAR")
            self.app.m_frame.apparent_power_std.SetLabel(str(std[5]) + " VA")
            self.app.m_frame.phase_angle_std.SetLabel(str(std[6]))
            self.app.m_frame.power_factor_std.SetLabel(str(std[7]))

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

    def on_exit(self, evt=None):
        self.wattrlib.stop_threads()
        self.app.Exit()
