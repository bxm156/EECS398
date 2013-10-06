import wxversion
wxversion.ensureMinimal('2.9')

import wx
from main_controller import MainController
from threads.database_thread import DatabaseThread
import Queue


class wattrApp(wx.App):
    def OnInit(self):
        self.db_thread = DatabaseThread("test", Queue.Queue())
        self.db_thread.start()
        controller = MainController(self)
        return True

    def onExit(self):
        self.db_thread.join()
        super(wattrApp, self).onExit()

app = wattrApp(False)
app.MainLoop()
