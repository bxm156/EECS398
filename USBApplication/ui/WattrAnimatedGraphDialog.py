"""Subclass of AnimatedGraphDialog, which is generated by wxFormBuilder."""
from pylab import num2date
from matplotlib import ticker
import datetime
import wx
import WattrGUI
import numpy
from lib.types import READING
from ui.WattrControlBox import WattrControlBox
from ui.WattrGraphPanel import WattrGraphPanel
# Implementing AnimatedGraphDialog
class WattrAnimatedGraphDialog(WattrGUI.AnimatedGraphDialog):

    DEFAULT_X_MAX = 50
    DEFAULT_WIN_LENGTH = 50

    def __init__(self, parent):
        super(WattrAnimatedGraphDialog, self).__init__(parent)
        
        self.graph_panel = WattrGraphPanel(self)
        self.GetSizer().Prepend(self.graph_panel, 1, wx.LEFT | wx.TOP | wx.GROW, border = 1)

        self.min_x = WattrControlBox(self, "X Min", 0)
        self.max_x = WattrControlBox(self, "X Max", 100)
        self.min_y = WattrControlBox(self, "Y Min", 0)
        self.max_y = WattrControlBox(self, "Y Max", 100)

        self.controls_sizer.Add(self.min_x) 
        self.controls_sizer.Add(self.max_x) 
        self.controls_sizer.Add(self.min_y) 
        self.controls_sizer.Add(self.max_y) 
        self.controls_sizer.Fit(self)
        self.Fit()
        
        self.data = []

        self.redraw_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_redraw_timer, self.redraw_timer)
        self.pause_button.Bind(wx.EVT_BUTTON, self.on_pause_button)
        self.pause_button.Bind(wx.EVT_UPDATE_UI, self.on_update_pause_button)
        self.show_grid.Bind(wx.EVT_CHECKBOX, self.on_show_grid)
        self.paused = False

    def show_alert(self, text):
        self.alert_text.SetLabel(text)
        self.alert_panel.Show()
        self.Layout()

    def hide_alert(self):
        self.alert_panel.Hide()
        self.Layout()

    def on_show_grid(self, evt):
        self.draw_plot()

    def on_pause_button(self, evt):
        self.paused = not self.paused
        if self.paused:
            self.show_alert("Spike!")
        else:
            self.hide_alert()

    def on_update_pause_button(self, evt):
        text = "Resume" if self.paused else "Pause"
        self.pause_button.SetLabel(text)

    def init_plot(self, rtype, y, title):
        self.rtype = rtype
        self.axes = self.graph_panel.add_plot()
        self.axes.set_title(title)
        self.axes.set_ylabel(y)
        self.axes.set_axis_bgcolor('black')
        self.plot_data = self.axes.plot(self.data,
            linewidth=1,
            color=(1,1,0),
        )[0]
        return
        def format_date(x, pos=None):
            if x <= 0:
                return "0"
            return num2date(x).strftime("%H:%M:%S")
        self.axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))

    def draw_plot(self):
        cols = zip(*self.data)
        if not cols:
            print "No Data"
            return
        x_data = cols[0]
        y_data = cols[1]

        if self.rtype == READING.VOLTAGE:
            if max(y_data) > 121:
                self.show_alert("Spike Detected!")
            if min(y_data) < 114:
                self.show_alert("Sag Detected!")

        if self.max_x.is_auto():
           xmax = x_data[-1] #if len(x_data) > self.DEFAULT_X_MAX else datetime.datetime.now()
        else:
            xmax = datetime.datetime.now() + datetime.timedelta(seconds=int(self.max_x.manual_value()))

        if self.min_x.is_auto():
            xmin = xmax - datetime.timedelta(seconds=50)
        else:
            xmin = datetime.datetime.now() + datetime.timedelta(seconds=int(self.min_x.manual_value()))

        if self.min_y.is_auto():
            ymin = round(min(y_data), 0) -1
        else:
            ymin = int(self.min_y.manual_value())

        if self.max_y.is_auto():
            ymax = round(max(y_data), 0) + 1
        else:
            ymax = int(self.max_y.manual_value())

        self.axes.set_xbound(lower=xmin, upper=xmax)
        self.axes.set_ybound(lower=ymin, upper=ymax)
        self.axes.relim()
        if self.show_grid.IsChecked():
            self.axes.grid(True, color='gray')
        else:
            self.axes.grid(False)
        self.plot_data.set_data(x_data, y_data)
        self.graph_panel.figure.autofmt_xdate()
        self.Layout()

    def on_redraw_timer(self, evt):
        if not self.paused:
            while True:
                value = self.data_source.next_reading(self.rtype)
                if value:
                    self.data.append(value)
                else:
                    break
        self.draw_plot()

    def start(self, data_source):
        self.data_source = data_source
        self.redraw_timer.Start(100)

    def stop(self):
        self.redraw_timer.Stop()
