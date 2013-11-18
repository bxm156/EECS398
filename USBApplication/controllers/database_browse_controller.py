import wx

from controllers.base_controller import BaseController
from ui.WattrDatabaseSelectorDialog import WattrDatabaseSelectorDialog


class DatabaseBrowseController(BaseController):

    view_class = WattrDatabaseSelectorDialog

    def __init__(self, parent, listener=None):
        super(DatabaseBrowseController, self).__init__(parent, listener)
        self.get_view().cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.get_view().browse_button.Bind(wx.EVT_BUTTON, self.on_browse)
        self.get_view().continue_button.Bind(wx.EVT_BUTTON, self.on_continue)

    def on_cancel(self, evt):
        self.get_view().EndModal(1)

    def on_browse(self, evt):
        openFileDialog = wx.FileDialog(self.get_view(), "Open", "", "", 
                                       "Database files (*.db)|*.db", 
                                       wx.FD_OPEN | wx.FILE_MUST_EXIST )
        openFileDialog.ShowModal()
        path = openFileDialog.GetPath()
        openFileDialog.Destroy()
        self.get_view().database_path.SetValue(path)

    def on_continue(self, evt):
        path = self.get_view().database_path.GetValue()
        self.listener.on_database_selected(path)
        self.get_view().EndModal(0)
