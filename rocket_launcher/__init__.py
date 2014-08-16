from lunchinator.plugin import iface_general_plugin
from lunchinator import get_server, log_info, log_error
    
class rocket_launcher(iface_general_plugin):    
    def __init__(self):
        super(rocket_launcher, self).__init__()
        
    def activate(self):        
        iface_general_plugin.activate(self)
        
        from pyrocket_backend import RocketManager
        self.rocket_controller = RocketManager()
    
        err_msg = self.rocket_controller.acquire_devices()
        if err_msg:
            raise Exception(err_msg)
        
        self.launcher = self.rocket_controller.launchers[0]
        
    def deactivate(self):
        iface_general_plugin.deactivate(self)        
    
    def process_event(self, cmd, value, ip, member_info):
        if cmd == "HELO_USBROCKET":
            log_error("FIRE!")
            self.launcher.start_movement(4)

