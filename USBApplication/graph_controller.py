
from ui.WattrGraphPanel import WattrGraphPanel

class GraphController(object):

    def __init__(self, parent):
        super(GraphController, self).__init__()
        self.panel = WattrGraphPanel(parent)

    def get_view(self):
        return self.panel
    
    def graph(self):
        self.panel.plot_data([1,2,3], [1,2,3], linewidth=2.0)
        self.panel.Show()



        
        
