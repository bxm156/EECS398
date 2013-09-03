import wx
from WatterMainFrame import WatterMainFrame


class watterApp(wx.App):
    def OnInit(self):
        self.m_frame = WatterMainFrame(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = watterApp(0)
app.MainLoop()
