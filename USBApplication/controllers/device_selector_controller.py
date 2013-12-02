import csv
import wx

from serial.tools import list_ports
from controllers.base_controller import BaseController
from ui.WattrDeviceSelectorDialog import WattrDeviceSelectorDialog


class DeviceSelectorController(BaseController):

    view_class = WattrDeviceSelectorDialog

    def __init__(self, parent, listener):
        super(DeviceSelectorController, self).__init__(parent, listener)
        self.listener = listener
        self.panel.cancel_device_selection.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.panel.refresh.Bind(wx.EVT_BUTTON, self.on_refresh)
        self.panel.device_choice.Bind(wx.EVT_CHOICE, self.update_select_state)
        self.panel.select_device.Bind(wx.EVT_BUTTON, self.on_select)
        self.list_devices()

    def on_close(self, evt):
        super(DeviceSelectorController, self).on_close(evt)
        self.listener.exit()

    def list_devices(self):
        self.panel.device_choice.Clear()
        self.panel.device_choice.Insert('None', 0)
        devs = [d[0] for d in list_ports.comports()]
        self.panel.device_choice.AppendItems(devs)
    
    def on_cancel(self, event):
       self.listener.exit()

    def on_select(self, event):
        current_selection = self.panel.device_choice.GetCurrentSelection()
        selected_string = self.panel.device_choice.GetString(current_selection)
        self.listener.on_device_selected(selected_string)
        self.get_view().EndModal(0)
        self.get_view().Destroy()


    def update_select_state(self, event):
        current_selection = self.panel.device_choice.GetCurrentSelection()
        if current_selection == 0:
            self.panel.select_device.Enable(False)
        else:
            self.panel.select_device.Enable(True)

    def on_refresh(self, event):
        self.list_devices()
        self.update_select_state(None)
