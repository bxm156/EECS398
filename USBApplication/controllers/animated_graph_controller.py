import wx

from controllers.base_controller import BaseController
from ui.WattrAnimatedGraphDialog import WattrAnimatedGraphDialog

class AnimatedGraphController(BaseController):

    view_class = WattrAnimatedGraphDialog

    def __init__(self, parent, wattrlib, listener=None):
        super(AnimatedGraphController, self).__init__(parent, listener=listener)
        self.wattrlib = wattrlib
        self.wattrlib.start_realtime_collection()
        self.data_source = self.wattrlib.get_realtime_store()
        self.get_view().init_plot()
        self.get_view().start(self.data_source)

    def on_close(self, evt):
        self.wattrlib.stop_realtime_collection()
        self.get_view().stop()
        super(AnimatedGraphController, self).on_close(evt)
