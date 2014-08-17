from PyQt4.QtGui import QWidget
from ui_launcher import Ui_LauncherWidget

class rocketWidget(QWidget):
    def __init__(self, parent, sendCommandClass):
        super(rocketWidget, self).__init__(parent)
        self.sendCommandClass = sendCommandClass
        self.ui = Ui_LauncherWidget()
        self.ui.setupUi(self)
        
    def left_clicked(self):
        pass
    def right_clicked(self):
        pass
    def up_clicked(self):
        pass
    def down_clicked(self):
        pass
    def fire_clicked(self):
        self.sendCommandClass.send_fire()