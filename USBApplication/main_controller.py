from ui.WattrMainFrame import WattrMainFrame
from graph_controller import GraphController

class MainController(object):

    def __init__(self, app):
        super(MainController, self).__init__()
        app.m_frame = WattrMainFrame(None)
        app.m_frame.Show()
        graph_controller = GraphController(app.m_frame.m_panel4)
        app.m_frame.m_panel4 = graph_controller.get_view()
        graph_controller.graph()
        app.SetTopWindow(app.m_frame)
