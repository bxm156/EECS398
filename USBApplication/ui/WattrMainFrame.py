"""Subclass of MainFrame, which is generated by wxFormBuilder."""
import datetime
import wx
from wx.lib.masked.timectrl import TimeCtrl
import WattrGUI


# Implementing MainFrame
class WattrMainFrame(WattrGUI.MainFrame):

    def __init__(self, parent):
        super(WattrMainFrame, self).__init__(parent)
        date_picker_container = self.m_panel_stats_date_pickers
        date_picker_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #Start Date/Time
        start_text = wx.StaticText(date_picker_container, wx.ID_ANY, u"Start Date/Time:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.start_date_picker = wx.DatePickerCtrl(date_picker_container, wx.ID_ANY, wx.DateTimeFromTimeT(1), wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_SHOWCENTURY)
        self.start_time_spinner = wx.SpinButton( self.m_panel_stats, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.start_time_picker = TimeCtrl(date_picker_container, wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, spinButton=self.start_time_spinner, limited=False, oob_color='white')

        #Add Start Date/Time to Panel
        date_picker_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        date_picker_sizer.Add(start_text, 0, wx.TOP, 10)
        date_picker_sizer.Add(self.start_date_picker, 0, wx.ALL, 5)
        date_picker_sizer.Add(self.start_time_picker, 0, wx.TOP|wx.RIGHT, 10)
        date_picker_sizer.Add(self.start_time_spinner, 0, wx.TOP, 14)
        date_picker_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        date_picker_container.SetSizerAndFit(date_picker_sizer)

        # Add seperator
        date_picker_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        #End Date/Time
        end_text = wx.StaticText(date_picker_container, wx.ID_ANY, u"End Date/Time:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.end_date_picker = wx.DatePickerCtrl(date_picker_container, wx.ID_ANY, wx.DateTime.Today(), wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_SHOWCENTURY)
        self.end_time_spinner = wx.SpinButton( self.m_panel_stats, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.end_time_picker = TimeCtrl(date_picker_container, wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, spinButton=self.end_time_spinner, limited=False, value='23:59:59', oob_color='white')

        #Add End Date/Time to Panel
        date_picker_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        date_picker_sizer.Add(end_text, 0, wx.TOP, 10)
        date_picker_sizer.Add(self.end_date_picker, 0, wx.ALL, 5)
        date_picker_sizer.Add(self.end_time_picker, 0, wx.TOP|wx.RIGHT, 10)
        date_picker_sizer.Add(self.end_time_spinner, 0, wx.TOP, 14)
        date_picker_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        date_picker_container.SetSizerAndFit(date_picker_sizer)

        # Update Button
        self.stats_update_button = wx.Button(date_picker_container, wx.ID_ANY,u"Update", wx.DefaultPosition, wx.DefaultSize, 0)
        date_picker_sizer.Add(self.stats_update_button, 0, wx.TOP, 10)
