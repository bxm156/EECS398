"""Subclass of HistogramDialog, which is generated by wxFormBuilder."""

import wx
import WattrGUI

# Implementing HistogramDialog
class WattrHistogramDialog( WattrGUI.HistogramDialog ):
	def __init__( self, parent ):
		WattrGUI.HistogramDialog.__init__( self, parent )
	
