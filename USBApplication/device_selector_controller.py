import csv
import wx

from serial.tools import list_ports

from ui.WattrDeviceSelectorFrame import WattrDeviceSelectorFrame


class DeviceSelectorController(object):

    def __init__(self, parent):
        super(DeviceSelectorController, self).__init__()
        self.frame = WattrDeviceSelectorFrame(parent)
        self.frame.cancel_device_selection.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.frame.refresh.Bind(wx.EVT_BUTTON, self.on_refresh)
        self.frame.device_choice.Bind(wx.EVT_CHOICE, self.update_select_state)
        self.list_devices()

    def get_view(self):
        return self.frame

    def list_devices(self):
        self.frame.device_choice.Clear()
        self.frame.device_choice.Insert('None', 0)
        devs = [d[0] for d in list_ports.comports()]
        self.frame.device_choice.AppendItems(devs)
    
    def on_cancel(self, event):
       self.frame.Destroy() 

    def update_select_state(self, event):
        current_selection = self.frame.device_choice.GetCurrentSelection()
        if current_selection == 0:
            self.frame.select_device.Enable(False)
        else:
            self.frame.select_device.Enable(True)

    def on_refresh(self, event):
        self.list_devices()
        self.update_select_state(None)
