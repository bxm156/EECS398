"""Subclass of DatabaseDialog, which is generated by wxFormBuilder."""

import wx
import WattrGUI

# Implementing DatabaseDialog
class WattrDatabaseDialog( WattrGUI.DatabaseDialog ):
	def __init__( self, parent ):
		WattrGUI.DatabaseDialog.__init__( self, parent )
	
