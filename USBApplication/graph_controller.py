import csv
import wx
from ui.WattrGraphPanel import WattrGraphPanel

class GraphController(object):

    def __init__(self, parent):
        super(GraphController, self).__init__()
        self.panel = WattrGraphPanel(parent)
        self.panel.import_csv.Bind(wx.EVT_BUTTON, self.on_import_csv)

    def get_view(self):
        return self.panel
    
    def graph(self, x=[1,2,3], y=[1,2,3]):
        self.panel.plot_data(x, y, linewidth=2.0)
        self.panel.Show()

    def on_import_csv(self, event):
        openFileDialog = wx.FileDialog(self.panel, "Open", "", "", 
                                       "CSV files (*.csv)|*.csv", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        path = openFileDialog.GetPath()
        openFileDialog.Destroy()

        with open(path, 'rb') as csv_input:
            graphdata = csv.DictReader(csv_input, fieldnames= ('time', 'voltage',))
            graphdata.next()
            x = []
            y = []
            for row in graphdata:
                x.append(float(row['time']))
                y.append(float(row['voltage']))
        self.graph(x, y)



        
        
