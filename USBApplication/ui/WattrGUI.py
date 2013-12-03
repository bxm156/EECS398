# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov 27 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Wattr", pos = wx.DefaultPosition, size = wx.Size( 800,550 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer7.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.device_conn_status = wx.StaticText( self, wx.ID_ANY, u"Connected", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_conn_status.Wrap( -1 )
		bSizer7.Add( self.device_conn_status, 0, wx.ALL, 5 )
		
		self.disconnect_button = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.disconnect_button, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText79 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )
		fgSizer3.Add( self.m_staticText79, 0, wx.ALL, 5 )
		
		self.device_latest_time = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_time.Wrap( -1 )
		fgSizer3.Add( self.device_latest_time, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"RMS Voltage:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.device_latest_voltage = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_voltage.Wrap( -1 )
		fgSizer3.Add( self.device_latest_voltage, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"RMS Current:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.device_latest_current = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_current.Wrap( -1 )
		fgSizer3.Add( self.device_latest_current, 0, wx.ALL, 5 )
		
		self.m_staticText81 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Period", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		fgSizer3.Add( self.m_staticText81, 0, wx.ALL, 5 )
		
		self.device_latest_period = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_period.Wrap( -1 )
		fgSizer3.Add( self.device_latest_period, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Active Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.device_latest_active_power = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_active_power.Wrap( -1 )
		fgSizer3.Add( self.device_latest_active_power, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Reactive Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.device_latest_reactive_power = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_reactive_power.Wrap( -1 )
		fgSizer3.Add( self.device_latest_reactive_power, 0, wx.ALL, 5 )
		
		self.m_staticText141 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Apparent Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		fgSizer3.Add( self.m_staticText141, 0, wx.ALL, 5 )
		
		self.device_latest_apparent_power = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_apparent_power.Wrap( -1 )
		fgSizer3.Add( self.device_latest_apparent_power, 0, wx.ALL, 5 )
		
		self.m_staticText83 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Phase Angle:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )
		fgSizer3.Add( self.m_staticText83, 0, wx.ALL, 5 )
		
		self.device_latest_phase_angle = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_phase_angle.Wrap( -1 )
		fgSizer3.Add( self.device_latest_phase_angle, 0, wx.ALL, 5 )
		
		self.m_staticText85 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Power Factor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		fgSizer3.Add( self.m_staticText85, 0, wx.ALL, 5 )
		
		self.device_latest_power_factor = wx.StaticText( self.m_panel5, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.device_latest_power_factor.Wrap( -1 )
		fgSizer3.Add( self.device_latest_power_factor, 0, wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( fgSizer3 )
		self.m_panel5.Layout()
		fgSizer3.Fit( self.m_panel5 )
		bSizer9.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer6 )
		self.m_panel1.Layout()
		bSizer6.Fit( self.m_panel1 )
		self.m_notebook4.AddPage( self.m_panel1, u"Device", False )
		self.m_panel_stats = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_panel_stats_box_sizer = wx.BoxSizer( wx.VERTICAL )
		
		date_picker_box_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel_stats_date_pickers = wx.Panel( self.m_panel_stats, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		date_picker_box_sizer.Add( self.m_panel_stats_date_pickers, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		m_panel_stats_box_sizer.Add( date_picker_box_sizer, 0, wx.EXPAND, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer12 = wx.FlexGridSizer( 0, 8, 5, 10 )
		fgSizer12.AddGrowableCol( 6 )
		fgSizer12.SetFlexibleDirection( wx.BOTH )
		fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer12.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText116 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Mean", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )
		fgSizer12.Add( self.m_staticText116, 0, wx.ALL, 5 )
		
		self.m_staticText117 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Median", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText117.Wrap( -1 )
		fgSizer12.Add( self.m_staticText117, 0, wx.ALL, 5 )
		
		self.m_staticText118 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText118.Wrap( -1 )
		fgSizer12.Add( self.m_staticText118, 0, wx.ALL, 5 )
		
		self.m_staticText119 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Maximum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText119.Wrap( -1 )
		fgSizer12.Add( self.m_staticText119, 0, wx.ALL, 5 )
		
		self.m_staticText120 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Minimum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText120.Wrap( -1 )
		fgSizer12.Add( self.m_staticText120, 0, wx.ALL, 5 )
		
		self.m_staticText184 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Std.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText184.Wrap( -1 )
		fgSizer12.Add( self.m_staticText184, 0, wx.ALL, 5 )
		
		
		fgSizer12.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText1213 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"RMS Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1213.Wrap( -1 )
		fgSizer12.Add( self.m_staticText1213, 0, wx.ALL, 5 )
		
		self.voltage_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.voltage_mean.Wrap( -1 )
		fgSizer12.Add( self.voltage_mean, 0, wx.ALL, 5 )
		
		self.voltage_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.voltage_median.Wrap( -1 )
		fgSizer12.Add( self.voltage_median, 0, wx.ALL, 5 )
		
		self.voltage_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.voltage_mode.Wrap( -1 )
		fgSizer12.Add( self.voltage_mode, 0, wx.ALL, 5 )
		
		self.voltage_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.voltage_max.Wrap( -1 )
		fgSizer12.Add( self.voltage_max, 0, wx.ALL, 5 )
		
		self.voltage_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.voltage_min.Wrap( -1 )
		fgSizer12.Add( self.voltage_min, 0, wx.ALL, 5 )
		
		self.voltage_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.voltage_std.Wrap( -1 )
		fgSizer12.Add( self.voltage_std, 0, wx.ALL, 5 )
		
		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.voltage_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.voltage_histogram, 0, wx.ALL, 5 )
		
		self.graph_voltage = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer38.Add( self.graph_voltage, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer38, 1, wx.EXPAND, 5 )
		
		self.m_staticText127 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"RMS Current", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText127.Wrap( -1 )
		fgSizer12.Add( self.m_staticText127, 0, wx.ALL, 5 )
		
		self.current_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.current_mean.Wrap( -1 )
		fgSizer12.Add( self.current_mean, 0, wx.ALL, 5 )
		
		self.current_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.current_median.Wrap( -1 )
		fgSizer12.Add( self.current_median, 0, wx.ALL, 5 )
		
		self.current_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.current_mode.Wrap( -1 )
		fgSizer12.Add( self.current_mode, 0, wx.ALL, 5 )
		
		self.current_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.current_max.Wrap( -1 )
		fgSizer12.Add( self.current_max, 0, wx.ALL, 5 )
		
		self.current_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.current_min.Wrap( -1 )
		fgSizer12.Add( self.current_min, 0, wx.ALL, 5 )
		
		self.current_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.current_std.Wrap( -1 )
		fgSizer12.Add( self.current_std, 0, wx.ALL, 5 )
		
		bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.current_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.current_histogram, 0, wx.ALL, 5 )
		
		self.graph_current = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.graph_current, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		self.m_staticText166 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Period", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText166.Wrap( -1 )
		fgSizer12.Add( self.m_staticText166, 0, wx.ALL, 5 )
		
		self.period_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_mean.Wrap( -1 )
		fgSizer12.Add( self.period_mean, 0, wx.ALL, 5 )
		
		self.period_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_median.Wrap( -1 )
		fgSizer12.Add( self.period_median, 0, wx.ALL, 5 )
		
		self.period_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_mode.Wrap( -1 )
		fgSizer12.Add( self.period_mode, 0, wx.ALL, 5 )
		
		self.period_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_max.Wrap( -1 )
		fgSizer12.Add( self.period_max, 0, wx.ALL, 5 )
		
		self.period_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_min.Wrap( -1 )
		fgSizer12.Add( self.period_min, 0, wx.ALL, 5 )
		
		self.period_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_std.Wrap( -1 )
		fgSizer12.Add( self.period_std, 0, wx.ALL, 5 )
		
		bSizer40 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.period_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.period_histogram, 0, wx.ALL, 5 )
		
		self.graph_period = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer40.Add( self.graph_period, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		self.m_staticText172 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Active Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )
		fgSizer12.Add( self.m_staticText172, 0, wx.ALL, 5 )
		
		self.active_power_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.active_power_mean.Wrap( -1 )
		fgSizer12.Add( self.active_power_mean, 0, wx.ALL, 5 )
		
		self.active_power_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.active_power_median.Wrap( -1 )
		fgSizer12.Add( self.active_power_median, 0, wx.ALL, 5 )
		
		self.active_power_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.active_power_mode.Wrap( -1 )
		fgSizer12.Add( self.active_power_mode, 0, wx.ALL, 5 )
		
		self.active_power_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.active_power_max.Wrap( -1 )
		fgSizer12.Add( self.active_power_max, 0, wx.ALL, 5 )
		
		self.active_power_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.active_power_min.Wrap( -1 )
		fgSizer12.Add( self.active_power_min, 0, wx.ALL, 5 )
		
		self.active_power_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.active_power_std.Wrap( -1 )
		fgSizer12.Add( self.active_power_std, 0, wx.ALL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.active_power_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.active_power_histogram, 0, wx.ALL, 5 )
		
		self.graph_active_power = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.graph_active_power, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		self.m_staticText178 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Reactive Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )
		fgSizer12.Add( self.m_staticText178, 0, wx.ALL, 5 )
		
		self.reactive_power_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reactive_power_mean.Wrap( -1 )
		fgSizer12.Add( self.reactive_power_mean, 0, wx.ALL, 5 )
		
		self.reactive_power_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reactive_power_median.Wrap( -1 )
		fgSizer12.Add( self.reactive_power_median, 0, wx.ALL, 5 )
		
		self.reactive_power_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reactive_power_mode.Wrap( -1 )
		fgSizer12.Add( self.reactive_power_mode, 0, wx.ALL, 5 )
		
		self.reactive_power_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reactive_power_max.Wrap( -1 )
		fgSizer12.Add( self.reactive_power_max, 0, wx.ALL, 5 )
		
		self.reactive_power_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reactive_power_min.Wrap( -1 )
		fgSizer12.Add( self.reactive_power_min, 0, wx.ALL, 5 )
		
		self.reactive_power_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.reactive_power_std.Wrap( -1 )
		fgSizer12.Add( self.reactive_power_std, 0, wx.ALL, 5 )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.reactive_power_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.reactive_power_histogram, 0, wx.ALL, 5 )
		
		self.graph_reactive_power = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer42.Add( self.graph_reactive_power, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer42, 1, wx.EXPAND, 5 )
		
		self.m_staticText193 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Apparent Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText193.Wrap( -1 )
		fgSizer12.Add( self.m_staticText193, 0, wx.ALL, 5 )
		
		self.apparent_power_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.apparent_power_mean.Wrap( -1 )
		fgSizer12.Add( self.apparent_power_mean, 0, wx.ALL, 5 )
		
		self.apparent_power_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.apparent_power_median.Wrap( -1 )
		fgSizer12.Add( self.apparent_power_median, 0, wx.ALL, 5 )
		
		self.apparent_power_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.apparent_power_mode.Wrap( -1 )
		fgSizer12.Add( self.apparent_power_mode, 0, wx.ALL, 5 )
		
		self.apparent_power_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.apparent_power_max.Wrap( -1 )
		fgSizer12.Add( self.apparent_power_max, 0, wx.ALL, 5 )
		
		self.apparent_power_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.apparent_power_min.Wrap( -1 )
		fgSizer12.Add( self.apparent_power_min, 0, wx.ALL, 5 )
		
		self.apparent_power_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.apparent_power_std.Wrap( -1 )
		fgSizer12.Add( self.apparent_power_std, 0, wx.ALL, 5 )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.apparent_power_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.apparent_power_histogram, 0, wx.ALL, 5 )
		
		self.graph_apparent_power = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer43.Add( self.graph_apparent_power, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer43, 1, wx.EXPAND, 5 )
		
		self.m_staticText200 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Phase Angle", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText200.Wrap( -1 )
		fgSizer12.Add( self.m_staticText200, 0, wx.ALL, 5 )
		
		self.phase_angle_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phase_angle_mean.Wrap( -1 )
		fgSizer12.Add( self.phase_angle_mean, 0, wx.ALL, 5 )
		
		self.phase_angle_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phase_angle_median.Wrap( -1 )
		fgSizer12.Add( self.phase_angle_median, 0, wx.ALL, 5 )
		
		self.phase_angle_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phase_angle_mode.Wrap( -1 )
		fgSizer12.Add( self.phase_angle_mode, 0, wx.ALL, 5 )
		
		self.phase_angle_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phase_angle_max.Wrap( -1 )
		fgSizer12.Add( self.phase_angle_max, 0, wx.ALL, 5 )
		
		self.phase_angle_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phase_angle_min.Wrap( -1 )
		fgSizer12.Add( self.phase_angle_min, 0, wx.ALL, 5 )
		
		self.phase_angle_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.phase_angle_std.Wrap( -1 )
		fgSizer12.Add( self.phase_angle_std, 0, wx.ALL, 5 )
		
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.phase_angle_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.phase_angle_histogram, 0, wx.ALL, 5 )
		
		self.graph_phase_angle = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.graph_phase_angle, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer44, 1, wx.EXPAND, 5 )
		
		self.m_staticText207 = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"Power Factor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText207.Wrap( -1 )
		fgSizer12.Add( self.m_staticText207, 0, wx.ALL, 5 )
		
		self.power_factor_mean = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.power_factor_mean.Wrap( -1 )
		fgSizer12.Add( self.power_factor_mean, 0, wx.ALL, 5 )
		
		self.power_factor_median = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.power_factor_median.Wrap( -1 )
		fgSizer12.Add( self.power_factor_median, 0, wx.ALL, 5 )
		
		self.power_factor_mode = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.power_factor_mode.Wrap( -1 )
		fgSizer12.Add( self.power_factor_mode, 0, wx.ALL, 5 )
		
		self.power_factor_max = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.power_factor_max.Wrap( -1 )
		fgSizer12.Add( self.power_factor_max, 0, wx.ALL, 5 )
		
		self.power_factor_min = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.power_factor_min.Wrap( -1 )
		fgSizer12.Add( self.power_factor_min, 0, wx.ALL, 5 )
		
		self.power_factor_std = wx.StaticText( self.m_panel_stats, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.power_factor_std.Wrap( -1 )
		fgSizer12.Add( self.power_factor_std, 0, wx.ALL, 5 )
		
		bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.power_factor_histogram = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Histogram", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.power_factor_histogram, 0, wx.ALL, 5 )
		
		self.graph_power_factor = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Graph", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.graph_power_factor, 0, wx.ALL, 5 )
		
		
		fgSizer12.Add( bSizer45, 1, wx.EXPAND, 5 )
		
		
		bSizer37.Add( fgSizer12, 1, wx.EXPAND|wx.LEFT|wx.TOP, 5 )
		
		
		m_panel_stats_box_sizer.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		
		m_panel_stats_box_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer23.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.stats_dump_raw_data = wx.Button( self.m_panel_stats, wx.ID_ANY, u"Dump Raw Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.stats_dump_raw_data, 0, wx.ALL, 5 )
		
		
		m_panel_stats_box_sizer.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		
		self.m_panel_stats.SetSizer( m_panel_stats_box_sizer )
		self.m_panel_stats.Layout()
		m_panel_stats_box_sizer.Fit( self.m_panel_stats )
		self.m_notebook4.AddPage( self.m_panel_stats, u"Statistics", False )
		
		bSizer1.Add( self.m_notebook4, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button42 = wx.Button( self, wx.ID_ANY, u"Force Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button42, 0, wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"ver 0.2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer10.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_calibrate = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Calibrate", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_calibrate )
		
		self.m_settings = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_settings )
		
		self.m_quit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_quit )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class HistogramDialog
###########################################################################

class HistogramDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Histogram", pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MINIMIZE_BOX|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.SetSizer( bSizer38 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class GraphPanel
###########################################################################

class GraphPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		vert_sizer = wx.BoxSizer( wx.VERTICAL )
		
		
		self.SetSizer( vert_sizer )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class CalibrationFrame
###########################################################################

class CalibrationFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calibration Settings", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DatabaseDialog
###########################################################################

class DatabaseDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select or Create a Database", pos = wx.DefaultPosition, size = wx.Size( 500,125 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"To begin, you must create a database to store collected data, or you may select a preexisting one:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( 500 )
		bSizer20.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.create_button = wx.Button( self, wx.ID_ANY, u"Create New Database", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.create_button.SetDefault() 
		bSizer21.Add( self.create_button, 0, wx.ALL, 5 )
		
		self.browse_button = wx.Button( self, wx.ID_ANY, u"Select Existing Database...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.browse_button, 0, wx.ALL, 5 )
		
		
		bSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer20.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer20 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DeviceSelectorDialog
###########################################################################

class DeviceSelectorDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Device Selector", pos = wx.DefaultPosition, size = wx.Size( 450,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Select the device:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer8.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		device_choiceChoices = []
		self.device_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, device_choiceChoices, 0 )
		self.device_choice.SetSelection( 0 )
		bSizer10.Add( self.device_choice, 0, wx.ALL, 5 )
		
		self.refresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.refresh, 0, wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.cancel_device_selection = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cancel_device_selection.SetDefault() 
		bSizer9.Add( self.cancel_device_selection, 0, wx.ALL, 5 )
		
		self.select_device = wx.Button( self, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.select_device.Enable( False )
		
		bSizer9.Add( self.select_device, 0, wx.ALL, 5 )
		
		
		bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DatabaseSelectorDialog
###########################################################################

class DatabaseSelectorDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Select the database you wish to use:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer17.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.database_path = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
		bSizer18.Add( self.database_path, 1, wx.ALL, 5 )
		
		self.browse_button = wx.Button( self, wx.ID_ANY, u"Browse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.browse_button.SetDefault() 
		bSizer18.Add( self.browse_button, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancel_button = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.cancel_button, 0, wx.ALL, 5 )
		
		
		bSizer19.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.continue_button = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.continue_button, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ControlBox
###########################################################################

class ControlBox ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		static_box_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
		
		self.radio_auto = wx.RadioButton( self, wx.ID_ANY, u"Auto", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.radio_auto.SetValue( True ) 
		static_box_sizer.Add( self.radio_auto, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.radio_manual = wx.RadioButton( self, wx.ID_ANY, u"Manual", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.radio_manual, 0, wx.ALL, 5 )
		
		self.manual_text = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_PROCESS_ENTER )
		self.manual_text.Enable( False )
		
		bSizer33.Add( self.manual_text, 0, wx.ALL, 5 )
		
		
		static_box_sizer.Add( bSizer33, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( static_box_sizer )
		self.Layout()
		static_box_sizer.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class AnimatedGraphDialog
###########################################################################

class AnimatedGraphDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Graph", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pause_button = wx.Button( self, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.pause_button, 0, wx.ALL, 5 )
		
		self.show_grid = wx.CheckBox( self, wx.ID_ANY, u"Show Grid", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.show_grid, 0, wx.ALL, 5 )
		
		self.show_x = wx.CheckBox( self, wx.ID_ANY, u"Show X Label", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.show_x, 0, wx.ALL, 5 )
		
		
		bSizer23.Add( bSizer22, 0, wx.ALIGN_LEFT|wx.EXPAND, 5 )
		
		self.controls_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer23.Add( self.controls_sizer, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer23 )
		self.Layout()
		bSizer23.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

