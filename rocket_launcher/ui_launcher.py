# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher.ui'
#
# Created: Sun Aug 17 18:56:54 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LauncherWidget(object):
    def setupUi(self, LauncherWidget):
        LauncherWidget.setObjectName(_fromUtf8("LauncherWidget"))
        LauncherWidget.resize(301, 163)
        self.btn_left = QtGui.QPushButton(LauncherWidget)
        self.btn_left.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.btn_left.setObjectName(_fromUtf8("btn_left"))
        self.btn_fire = QtGui.QPushButton(LauncherWidget)
        self.btn_fire.setGeometry(QtCore.QRect(50, 110, 201, 23))
        self.btn_fire.setObjectName(_fromUtf8("btn_fire"))
        self.comboBox_peer = QtGui.QComboBox(LauncherWidget)
        self.comboBox_peer.setGeometry(QtCore.QRect(50, 10, 201, 22))
        self.comboBox_peer.setObjectName(_fromUtf8("comboBox_peer"))
        self.comboBox_peer.addItem(_fromUtf8(""))
        self.btn_right = QtGui.QPushButton(LauncherWidget)
        self.btn_right.setGeometry(QtCore.QRect(190, 50, 75, 23))
        self.btn_right.setObjectName(_fromUtf8("btn_right"))
        self.splitter = QtGui.QSplitter(LauncherWidget)
        self.splitter.setGeometry(QtCore.QRect(110, 35, 75, 51))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btn_up = QtGui.QPushButton(self.splitter)
        self.btn_up.setObjectName(_fromUtf8("btn_up"))
        self.btn_down = QtGui.QPushButton(self.splitter)
        self.btn_down.setObjectName(_fromUtf8("btn_down"))

        self.retranslateUi(LauncherWidget)
        QtCore.QObject.connect(self.btn_fire, QtCore.SIGNAL(_fromUtf8("clicked()")), LauncherWidget.fire_clicked)
        QtCore.QObject.connect(self.btn_up, QtCore.SIGNAL(_fromUtf8("clicked()")), LauncherWidget.up_clicked)
        QtCore.QObject.connect(self.btn_down, QtCore.SIGNAL(_fromUtf8("clicked()")), LauncherWidget.down_clicked)
        QtCore.QObject.connect(self.btn_right, QtCore.SIGNAL(_fromUtf8("clicked()")), LauncherWidget.right_clicked)
        QtCore.QObject.connect(self.btn_left, QtCore.SIGNAL(_fromUtf8("clicked()")), LauncherWidget.left_clicked)
        QtCore.QObject.connect(self.comboBox_peer, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), LauncherWidget.peer_change_clicked)
        QtCore.QMetaObject.connectSlotsByName(LauncherWidget)

    def retranslateUi(self, LauncherWidget):
        LauncherWidget.setWindowTitle(_translate("LauncherWidget", "Form", None))
        self.btn_left.setText(_translate("LauncherWidget", "<", None))
        self.btn_fire.setText(_translate("LauncherWidget", "FIRE!", None))
        self.comboBox_peer.setItemText(0, _translate("LauncherWidget", "All", None))
        self.btn_right.setText(_translate("LauncherWidget", ">", None))
        self.btn_up.setText(_translate("LauncherWidget", "^", None))
        self.btn_down.setText(_translate("LauncherWidget", "V", None))

