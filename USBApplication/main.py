import wxversion
wxversion.ensureMinimal('2.9')

import wx
from controllers.main_controller import MainController


class wattrApp(wx.App):
    """Main Application Class"""

    def OnInit(self):
        #Create the Main Controller for the app
        self.controller = MainController(self)
        return True

    def onExit(self):
        super(wattrApp, self).onExit()
        self.controller.on_exit()

#Create the app
app = wattrApp(False)

#Run the main GUI loop
app.MainLoop()
