from lunchinator.plugin import iface_gui_plugin
from lunchinator import get_server, log_info, log_error, log_exception, log_debug
from lunchinator.peer_actions import PeerAction
from threading import Timer
import os, json

class _FireRocketAction(PeerAction):
    def getName(self):
        return u"FireRocket"
    
    def appliesToPeer(self, _peerID, peerInfo):
        return u"hasUSBRocket" in peerInfo
    
    def performAction(self, peerID, _peerInfo, parentWidget):
        self.getPluginObject().send_command("FIRE", peerID)
        
    def getMessagePrefix(self):
        return "USBROCKET"
    
    def getConfirmationMessage(self, _peerID, peerName, msgData):        
        return u"%s wants to Control your USB Rocket Launcher" % (peerName)
    
class rocket_launcher(iface_gui_plugin):  
    VERSION_INITIAL = 0
    VERSION_CURRENT = VERSION_INITIAL
      
    def __init__(self):
        super(rocket_launcher, self).__init__()
        self.options = [(("remote_only","Only Remote Control", self.activate_rocket_launcher),True)]
        self.number_map = ["DOWN","UP","LEFT","RIGHT","FIRE","STOP"]
        
    def get_displayed_name(self):
        return u"USB Rocket Launcher"
        
    def activate(self):        
        iface_gui_plugin.activate(self)
        self._rocketAction = _FireRocketAction()
        self.launcher = None
        self.activate_rocket_launcher(False, self.options["remote_only"])
        
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
                log_exception("USB Rocket launcher could not be activated: ", e)
                self.launcher = None
                #-> problem while activating: only remote control!
                return True
            
        return newVal
                
    def deactivate(self):
        iface_gui_plugin.deactivate(self)       
        
    def get_peer_actions(self):
        return [self._rocketAction]         
    
    def process_event(self, cmd, value, ip, member_info, preprocessedData=None):
        if self.launcher:
            if cmd == "HELO_USBROCKET":
                try:
                    if value=="FIRE":
                        self.launcher.stop_movement()
                        self.launcher.start_movement(4)
                    else:
                        self.launcher.start_movement(self.number_map.index(value))
                        Timer(0.5, self.launcher.stop_movement).start()
                except ValueError as e:
                    log_debug("USB Rocket: Command value unknown: ", value)
    
    def extendsInfoDict(self):
        return True
    
    def extendInfoDict(self, infoDict):
        if self.launcher:
            infoDict[u"hasUSBRocket"] = not self.options["remote_only"]
    
    def create_widget(self, parent):       
        from rocket_widget import rocketWidget
        
        self.w = rocketWidget(parent, self)            
        return self.w
    
    def send_command(self, cmd, peerID = None):
        if peerID:
            get_server().call("HELO_USBROCKET %s"%cmd, peerIDs=[peerID])
        else:
            get_server().call("HELO_USBROCKET %s"%cmd)
