from PyQt4.QtGui import QWidget
from ui_launcher import Ui_LauncherWidget
from lunchinator import get_peers, log_warning
from functools import partial

class rocketWidget(QWidget):
    def __init__(self, parent, sendCommandClass):
        super(rocketWidget, self).__init__(parent)
        self.sendCommandClass = sendCommandClass
        self.ui = Ui_LauncherWidget()
        self.ui.setupUi(self)
        self._launcherPeerID = None
        
    def _changePeer(self, ID):
        self._launcherPeerID = ID

    def peer_change_clicked(self, index):
        pass
    
    def left_clicked(self):
        self.sendCommandClass.send_command("RIGHT", self._launcherPeerID)
    def right_clicked(self):
        self.sendCommandClass.send_command("LEFT", self._launcherPeerID)
    def up_clicked(self):
        self.sendCommandClass.send_command("UP", self._launcherPeerID)
    def down_clicked(self):
        self.sendCommandClass.send_command("DOWN", self._launcherPeerID)
    def fire_clicked(self):
        self.sendCommandClass.send_command("FIRE", self._launcherPeerID)