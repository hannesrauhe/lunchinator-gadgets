from lunchinator.plugin import iface_gui_plugin
from lunchinator import get_server, log_info, log_error, log_exception
from lunchinator.peer_actions import PeerAction
import os, json

class _FireRocketAction(PeerAction):
    def getName(self):
        return u"FireRocket"
    
    def appliesToPeer(self, _peerID, peerInfo):
        return u"USBROCKET_v" in peerInfo
    
    def performAction(self, peerID, _peerInfo, parentWidget):
        self.getPluginObject().send_fire(peerID)
        
    def getMessagePrefix(self):
        return "USBROCKET"
    
    def getConfirmationMessage(self, _peerID, peerName, msgData):        
        return u"%s wants to Fire the USB rocket" % (peerName)
    
class rocket_launcher(iface_gui_plugin):  
    VERSION_INITIAL = 0
    VERSION_CURRENT = VERSION_INITIAL
      
    def __init__(self):
        super(rocket_launcher, self).__init__()
        self.options = [(("remote_only","Only Remote Control", self.activate_rocket_launcher),True)]
        
    def activate(self):        
        iface_gui_plugin.activate(self)
        self._rocketAction = _FireRocketAction()
        self.launcher = None
        if not self.options["remote_only"]:
            self.activat_rocket_launcher()
        
    def activate_rocket_launcher(self, _setting, newVal):
        '''only called if not remote_only -> the rocket launcher is attached to this peer'''
        if not newVal:
            try:
                from pyrocket_backend import RocketManager
                self.rocket_controller = RocketManager()
             
                err_msg = self.rocket_controller.acquire_devices()
                if err_msg:
                    raise Exception(err_msg)
                 
                self.launcher = self.rocket_controller.launchers[0]
            except Exception as e:
                log_exception("USB Rocket launcher could not be activated: %s", e)
                #-> problem while activating: only remote control!
                return True
            
        return newVal
                
    def deactivate(self):
        iface_gui_plugin.deactivate(self)       
        
    def get_peer_actions(self):
        return [self._rocketAction]         
    
    def process_event(self, cmd, value, ip, member_info, preprocessedData=None):
        if self.options["remote_only"]:
            if cmd == "HELO_USBROCKET":
                log_error("FIRE!")
    #             self.launcher.start_movement(4)
    
    def extendInfoDict(self, infoDict):
        if self.launcher:
            infoDict[u"hasUSBRocket"] = not self.options["remote_only"]
    
    def create_widget(self, parent):       
        from rocket_widget import rocketWidget
        
        self.w = rocketWidget(parent, self)            
        return self.w
    
    def send_fire(self, peerID = None):
        if peerID:
            get_server().call("HELO_USBROCKET FIRE", peerIDs=[peerID])
        else:
            get_server().call("HELO_USBROCKET FIRE")
