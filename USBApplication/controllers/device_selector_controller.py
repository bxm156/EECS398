import csv
import wx

from serial.tools import list_ports

from ui.WattrDeviceSelectorDialog import WattrDeviceSelectorDialog


class DeviceSelectorController(object):

    def __init__(self, parent, listener):
        super(DeviceSelectorController, self).__init__()
        self.listener = listener
        self.frame = WattrDeviceSelectorDialog(parent)
        self.frame.cancel_device_selection.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.frame.refresh.Bind(wx.EVT_BUTTON, self.on_refresh)
        self.frame.device_choice.Bind(wx.EVT_CHOICE, self.update_select_state)
        self.frame.select_device.Bind(wx.EVT_BUTTON, self.on_select)
        self.list_devices()

    def get_view(self):
        return self.frame

    def list_devices(self):
        self.frame.device_choice.Clear()
        self.frame.device_choice.Insert('None', 0)
        devs = [d[0] for d in list_ports.comports()]
        self.frame.device_choice.AppendItems(devs)
    
    def on_cancel(self, event):
       self.listener.exit()

    def on_select(self, event):
        current_selection = self.frame.device_choice.GetCurrentSelection()
        selected_string = self.frame.device_choice.GetString(current_selection)
        self.listener.on_device_selected(selected_string)
        self.get_view().EndModal(0)


    def update_select_state(self, event):
        current_selection = self.frame.device_choice.GetCurrentSelection()
        if current_selection == 0:
            self.frame.select_device.Enable(False)
        else:
            self.frame.select_device.Enable(True)

    def on_refresh(self, event):
        self.list_devices()
        self.update_select_state(None)
