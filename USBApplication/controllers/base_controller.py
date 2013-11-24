import wx

class BaseController(object):

    view_class = None

    def __init__(self, parent, listener=None):
        super(BaseController, self).__init__()
        assert self.view_class
        self.panel = self.view_class(parent)
        self.panel.Bind(wx.EVT_CLOSE, self.on_close)
        self.listener = listener

    def get_view(self):
        return self.panel

    def on_close(self, evt):
        self.panel.Destroy()
