class BaseController(object):

    view_class = None

    def __init__(self, parent, listener=None):
        super(BaseController, self).__init__()
        assert self.view_class
        self.panel = self.view_class(parent)
        self.listener = listener

    def get_view(self):
        return self.panel
