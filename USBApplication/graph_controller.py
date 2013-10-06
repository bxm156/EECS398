
from ui.WattrGraphPanel import WattrGraphPanel

class GraphController(object):

    def __init__(self, parent):
        super(GraphController, self).__init__()
        self.panel = WattrGraphPanel(parent)

    def get_view(self):
        return self.panel
    
    def graph(self):
        self.panel.init_plot_data()
        self.panel.Show()



        
        
