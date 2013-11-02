import wx

from controllers.base_controller import BaseController
from controllers.database_browse_controller import DatabaseBrowseController
from ui.WattrDatabaseFrame import WattrDatabaseFrame


class DatabaseController(BaseController):

    view_class = WattrDatabaseFrame

    def __init__(self, parent, listener):
        super(DatabaseController, self).__init__(parent, listener)
        # Bind buttons
        self.get_view().create_button.Bind(wx.EVT_BUTTON, self.on_create)
        self.get_view().browse_button.Bind(wx.EVT_BUTTON, self.on_browse)

    def on_create(self, evt):
        createFileDialog = wx.FileDialog(self.get_view(), "Create", "", "", 
                                       "Database files (*.db)|*.db", 
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        createFileDialog.ShowModal()
        path = createFileDialog.GetPath()
        createFileDialog.Destroy()
        self.panel.Destroy()

    def on_browse(self, evt):
        browse_controller = DatabaseBrowseController(self.get_view(), self)
        browse_controller.get_view().Show()

