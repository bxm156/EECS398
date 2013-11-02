import wxversion
wxversion.ensureMinimal('2.9')

import wx
from controllers.main_controller import MainController


class wattrApp(wx.App):
    def OnInit(self):
        self.controller = MainController(self)
        return True

    def onExit(self):
        super(wattrApp, self).onExit()
        self.controller.on_exit()

app = wattrApp(False)
app.MainLoop()
