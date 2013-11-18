import wx

from controllers.base_controller import BaseController
from controllers.database_browse_controller import DatabaseBrowseController
from ui.WattrDatabaseDialog import WattrDatabaseDialog


class DatabaseController(BaseController):

    view_class = WattrDatabaseDialog

    def __init__(self, parent, listener):
        super(DatabaseController, self).__init__(parent, listener)
        # Bind buttons
        self.get_view().create_button.Bind(wx.EVT_BUTTON, self.on_create)
        self.get_view().browse_button.Bind(wx.EVT_BUTTON, self.on_browse)
        self.listener = listener

    def on_create(self, evt):
        createFileDialog = wx.FileDialog(self.get_view(), "Create", "", "", 
                                       "Database files (*.db)|*.db", 
                                       wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if createFileDialog.ShowModal() != wx.ID_CANCEL:
            path = createFileDialog.GetPath()
            createFileDialog.Destroy()
            self.listener.on_database_selected(path)
            self.get_view().EndModal(0)

    def on_browse(self, evt):
        browse_controller = DatabaseBrowseController(self.get_view(), self.listener)
        browse_canceled = browse_controller.get_view().ShowModal()
        if not browse_canceled:
            self.get_view().EndModal(0)

