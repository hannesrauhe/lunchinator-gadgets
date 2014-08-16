from lunchinator.plugin import iface_gui_plugin
from lunchinator import get_server, log_info, log_error
    
class rocket_launcher_gui(iface_gui_plugin):    
    def __init__(self):
        super(rocket_launcher_gui, self).__init__()
        
    def activate(self):        
        iface_gui_plugin.activate(self)
        
        
    def deactivate(self):
        iface_gui_plugin.deactivate(self)

