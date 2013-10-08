"""Subclass of GraphPanel, which is generated by wxFormBuilder."""
import matplotlib
matplotlib.use('WXAgg')
import matplotlib.cm as cm
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
from matplotlib.figure import Figure
import wx
import wx.xrc as xrc
matplotlib.rc('image', origin='lower')
import numpy as np

import WattrGUI


# Implementing GraphPanel
class WattrGraphPanel( WattrGUI.GraphPanel ):

    def __init__(self, parent, fgsize=None, dpi=None):
        super(WattrGraphPanel, self).__init__(parent)
        self.figure = Figure(fgsize, dpi)

        #Transparent figure face color
        self.figure.set_facecolor((0,0,0,0,))


        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        # Now put all into a sizer
        sizer = self.GetSizer()
        # This way of adding to sizer allows resizing
        sizer.Add(self.canvas, 1, wx.LEFT|wx.TOP|wx.GROW)
        # Best to allow the toolbar to resize!
        self.Fit()

    def plot_data(self, x, y, **kwargs):
        self.plot.clear()
        self.plot.plot(x, y, **kwargs)
        self.figure.canvas.draw()

    def set_title(self, title):
        self.plot.set_title(title)

    def show_graph(self, boolean):
        self.plot.grid(boolean)

    def set_label_x(self, label):
       self.plot.set_xlabel(label)

    def set_label_y(self, label):
       self.plot.set_ylabel(label)
