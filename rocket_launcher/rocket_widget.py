from PyQt4.QtGui import QWidget
from ui_launcher import Ui_LauncherWidget

class rocketWidget(QWidget):
    def __init__(self, parent, sendCommandClass):
        super(rocketWidget, self).__init__(parent)
        self.sendCommandClass = sendCommandClass
        self.ui = Ui_LauncherWidget()
        self.ui.setupUi(self)
        
    def left_clicked(self):
        self.sendCommandClass.send_command("RIGHT")
    def right_clicked(self):
        self.sendCommandClass.send_command("LEFT")
    def up_clicked(self):
        self.sendCommandClass.send_command("UP")
    def down_clicked(self):
        self.sendCommandClass.send_command("DOWN")
    def fire_clicked(self):
        self.sendCommandClass.send_command("FIRE")