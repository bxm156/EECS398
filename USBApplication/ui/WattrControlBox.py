"""Subclass of ControlBox, which is generated by wxFormBuilder."""

import wx
import WattrGUI

# Implementing ControlBox
class WattrControlBox(WattrGUI.ControlBox):

    def __init__(self, parent, label, initval):
        super(WattrControlBox, self).__init__(parent)
        self.GetSizer().GetStaticBox().SetLabel(label)
        self.manual_text.SetValue(str(initval))
        self.value = initval

        self.Bind(wx.EVT_UPDATE_UI, self.on_update_buttons, self.manual_text)
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text, self.manual_text)

    def on_update_buttons(self, evt):
        self.manual_text.Enable(not self.is_auto())

    def on_text(self, evt):
        self.value = int(self.manual_text.GetValue())
        if self.value != self.manual_text.GetValue():
            self.manual_text.SetValue(str(self.value))
        
    def is_auto(self):
        return self.radio_auto.GetValue()

    def manual_value(self):
        return self.value