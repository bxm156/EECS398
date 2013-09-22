import wx
from ui.WattrMainFrame import WattrMainFrame
from threads.database_thread import DatabaseThread
import Queue


class wattrApp(wx.App):
    def OnInit(self):
        self.db_thread = DatabaseThread("test", Queue.Queue())
        self.db_thread.start()
        self.m_frame = WattrMainFrame(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

    def OnExit(self):
        self.db_thread.join()
        super(wattrApp, self).OnExit()

app = wattrApp(False)
app.MainLoop()
