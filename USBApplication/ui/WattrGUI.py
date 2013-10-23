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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Wattr", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer7.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Connected on COM1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer7.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		self.m_notebook4 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText10 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Voltage:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"5V", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Current:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer3.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"1A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer3.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Power:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer3.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"10W", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Power Factor:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_staticText131 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		fgSizer3.Add( self.m_staticText131, 0, wx.ALL, 5 )
		
		self.m_staticText141 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Frequency:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		fgSizer3.Add( self.m_staticText141, 0, wx.ALL, 5 )
		
		self.m_staticText151 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"10 MHz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		fgSizer3.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( fgSizer3 )
		self.m_panel5.Layout()
		fgSizer3.Fit( self.m_panel5 )
		bSizer9.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer6 )
		self.m_panel1.Layout()
		bSizer6.Fit( self.m_panel1 )
		self.m_notebook4.AddPage( self.m_panel1, u"Device", False )
		self.m_panel4 = wx.Panel( self.m_notebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		bSizer61.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer61 )
		self.m_panel4.Layout()
		bSizer61.Fit( self.m_panel4 )
		self.m_notebook4.AddPage( self.m_panel4, u"Graphs", False )
		
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
## Class GraphPanel
###########################################################################

class GraphPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		vert_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.import_csv = wx.Button( self, wx.ID_ANY, u"Import CSV", wx.DefaultPosition, wx.DefaultSize, 0 )
		vert_sizer.Add( self.import_csv, 0, wx.ALL, 5 )
		
		
		self.SetSizer( vert_sizer )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class CalibrationFrame
###########################################################################

class CalibrationFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calibration Settings", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DeviceSelectorFrame
###########################################################################

class DeviceSelectorFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Device Selector", pos = wx.DefaultPosition, size = wx.Size( 450,150 ), style = wx.CAPTION|wx.STAY_ON_TOP|wx.CLIP_CHILDREN|wx.TAB_TRAVERSAL )
		
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
	

