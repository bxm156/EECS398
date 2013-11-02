import wx

from controllers.base_controller import BaseController
from ui.WattrDatabaseSelectorFrame import WattrDatabaseSelectorFrame


class DatabaseBrowseController(BaseController):

    view_class = WattrDatabaseSelectorFrame

    def __init__(self, parent, listener=None):
        super(DatabaseBrowseController, self).__init__(parent, listener)
        self.get_view().cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.get_view().browse_button.Bind(wx.EVT_BUTTON, self.on_browse)
        self.get_view().continue_button.Bind(wx.EVT_BUTTON, self.on_continue)

    def on_cancel(self, evt):
        self.get_view().Destroy()

    def on_browse(self, evt):
        openFileDialog = wx.FileDialog(self.get_view(), "Open", "", "", 
                                       "Database files (*.db)|*.db", 
                                       wx.FD_OPEN | wx.FILE_MUST_EXIST )
        openFileDialog.ShowModal()
        path = openFileDialog.GetPath()
        openFileDialog.Destroy()
        self.get_view().database_path.SetValue(path)

    def on_continue(self, evt):
        pass

