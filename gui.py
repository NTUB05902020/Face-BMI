# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def createButton(self, widget, args, name):
        ret = QtWidgets.QPushButton(widget)
        left, up, width, height = args
        ret.setGeometry(QtCore.QRect(left, up, width, height))
        ret.setObjectName(name)
        return ret
        
    def setupUi(self, MainWindow):
        self.pics = []
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 1440, 1280))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        
        self.picNameLabel = QtWidgets.QLabel('                                  ', self.centralwidget)
        self.picNameLabel.move(1460, 150)
        self.picNameLabel.setFont(QtGui.QFont("Roman times", 12, QtGui.QFont.Bold))
        
        self.BMILabel = QtWidgets.QLabel('BMI:          ', self.centralwidget)
        self.BMILabel.move(1480, 400)
        self.BMILabel.setFont(QtGui.QFont("Roman times", 20, QtGui.QFont.Bold))
        
        self.predictButton = self.createButton(self.centralwidget, (1480, 850, 291, 81), "predictButton")
        self.browseButton = self.createButton(self.centralwidget, (1480, 1150, 291, 81), "browseButton")
        self.nextButton = self.createButton(self.centralwidget, (1480, 1050, 291, 81), "nextButton")
        self.prevButton = self.createButton(self.centralwidget, (1480, 950, 291, 81), "prevButton")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.firstRetranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.predictButton.clicked.connect(self.predict)
        self.browseButton.clicked.connect(self.openFileDialog)
        self.prevButton.clicked.connect(self.prevPic)
        self.nextButton.clicked.connect(self.nextPic)
        
    def firstRetranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseButton.setText(_translate("MainWindow", "browse"))
        self.nextButton.setText(_translate("MainWindow", "next"))
        self.prevButton.setText(_translate("MainWindow", "prev"))
        self.predictButton.setText(_translate("MainWindow", "predict"))
        
    def predict(self):
        self.BMILabel.setText("BMI:  22.0")
    
    def nextPic(self):
        if len(self.pics) > 0:
            self.indx = (self.indx + 1) % len(self.pics)
            self.photo.setPixmap(QtGui.QPixmap(os.path.join(self.dirName, self.pics[self.indx])))
            self.BMILabel.setText('BMI:          ')
            self.picNameLabel.setText(self.pics[self.indx])
    
    def prevPic(self):
        if len(self.pics) > 0:
            self.indx = (self.indx - 1) % len(self.pics)
            self.photo.setPixmap(QtGui.QPixmap(os.path.join(self.dirName, self.pics[self.indx])))
            self.BMILabel.setText('BMI:          ')
            self.picNameLabel.setText(self.pics[self.indx])
    
    def openFileDialog(self):
        self.dirName = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, 'Choose Directory', os.getcwd())
        self.pics = [pic for pic in os.listdir(self.dirName) if pic.endswith('.jpg')]
        if len(self.pics) > 0:
            self.indx = 0
            self.BMILabel.setText('BMI:          ')
            self.picNameLabel.setText(self.pics[self.indx])
            self.photo.setPixmap(QtGui.QPixmap(os.path.join(self.dirName, self.pics[self.indx])))
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
