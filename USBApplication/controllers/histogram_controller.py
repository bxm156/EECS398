import wx

from controllers.base_controller import BaseController
from ui.WattrGraphPanel import WattrGraphPanel
from ui.WattrHistogramDialog import WattrHistogramDialog

class HistogramController(BaseController):

    view_class = WattrHistogramDialog

    def __init__(self, parent, listener=None):
        super(HistogramController, self).__init__(parent, listener)
        self.histogram_panel = WattrGraphPanel(self.get_view())
        self.plot = self.histogram_panel.add_plot()
        sizer = self.get_view().GetSizer()
        sizer.Add(self.histogram_panel, 1, wx.LEFT|wx.TOP|wx.GROW, border=1)
        self.get_view().Fit()

    def plot_hist(self, data, title, x, y):
        self.plot.hist(data)
        self.plot.set_title(title)
        self.plot.set_xlabel(x)
        self.plot.set_ylabel(y)
        self.histogram_panel.figure.tight_layout()
        self.get_view().Fit()

    def on_close(self, evt):
        self.get_view().EndModal(0)



