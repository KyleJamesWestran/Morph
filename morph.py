from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
import time
import subprocess

class Ui_Form(object):
    def setupUi(self, Form):
        #UI Setup
        Form.setObjectName("Form")
        Form.resize(390, 280)
        Form.setMaximumSize(350, 10)
        Form.setMinimumSize(350, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        '''self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimumSize(327,10)
        self.progressBar.setMaximumSize(327, 10)
        self.progressBar.setTextVisible(False)
        self.gridLayout.addWidget(self.progressBar, 8, 0, 1, 3)'''
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap("Resources/Logo.png"))
        self.label.setScaledContents(True)
        self.label.setMaximumSize(350,150)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)
        self.btnBrowse = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Resources/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBrowse.setIcon(icon)
        self.btnBrowse.setIconSize(QtCore.QSize(12, 12))
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout.addWidget(self.btnBrowse, 4, 2, 1, 1)
        self.listTypes = QtWidgets.QComboBox(Form)
        self.listTypes.setObjectName("listTypes")

        self.listTypes.addItem("mp4")
        self.listTypes.addItem("avi")
        self.listTypes.addItem("mkv")
        self.listTypes.addItem("mov")
        #self.listTypes.addItem("mpg")
        self.listTypes.addItem("wmv")

        self.gridLayout.addWidget(self.listTypes, 6, 0, 1, 3)
        self.btnConvert = QtWidgets.QPushButton(Form)
        self.btnConvert.setMinimumSize(QtCore.QSize(0, 40))
        self.btnConvert.setObjectName("bntConvert")
        icon.addPixmap(QtGui.QPixmap("Resources/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConvert.setIcon(icon)
        self.btnConvert.setIconSize(QtCore.QSize(16, 16 ))
        self.gridLayout.addWidget(self.btnConvert, 7, 0, 1, 3)
        self.lblPath = QtWidgets.QLabel(Form)
        self.lblPath.setObjectName("label_3")
        self.gridLayout.addWidget(self.lblPath, 4, 0, 1, 2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #Call Functions
        self.btnBrowse.clicked.connect(lambda: browseFile(self))
        self.btnConvert.clicked.connect(lambda: getFormat(self))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Morph"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">File Location:</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Select conversion format:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#555753;\">CONVERT VIDEOS TO ANY SPECIFIED FORMAT</span></p></body></html>"))
        self.btnBrowse.setText(_translate("Form", " BROWSE"))
        self.btnConvert.setText(_translate("Form", " CONVERT"))
        self.lblPath.setText(_translate("Form", "Browse Files or folders"))

def browseFile(self):
    fileName = QFileDialog.getOpenFileName(self.lblPath, 'Open file','c:\\', "Video Files (*.avi *.mkv *.mov *.mp4 *.mpg *.wmv)")
    filePath = fileName[0]
    self.lblPath.setText(filePath)

def getFormat(self):
    filePath = self.lblPath.text()
    fileFormat = filePath[-4:]
    convertTo = self.listTypes.currentText()

    if (self.lblPath.text() == "Browse Files or folders") or (self.lblPath.text() == ""):
        browseMessage()
    else:
        #For AVI conversion
        if fileFormat == '.avi':
            if convertTo == 'mp4':
                avi_to_mp4(self,filePath)
                completeMessage(self)
            elif convertTo == 'mkv':
                avi_to_mkv(filePath)
                completeMessage(self)
            #elif convertTo == 'mpg':
                #avi_to_mpg(filePath)
            elif convertTo == 'mov':
                avi_to_mov(filePath)
                completeMessage(self)
            elif convertTo == 'wmv':
                avi_to_wmv(filePath)
                completeMessage(self)
            else:
                typeMessage()
        else:
            formatMessage(fileFormat)

#Convert functions
def avi_to_mp4(self, filePath):
    outputFile = (filePath.rstrip(filePath[-4:]))
    #print("converting avi to mp4")
    p = subprocess.Popen("ffmpeg -i {input} {output}.mp4".format(input=filePath, output=outputFile))
    waitMessage()
    p.wait()
    return True

def avi_to_mkv(filePath):
    outputFile = (filePath.rstrip(filePath[-4:]))
    #print("converting avi to mkv")
    p = subprocess.Popen("ffmpeg -i {input} {output}.mp4".format(input=filePath, output=outputFile))
    waitMessage()
    p.wait()
    return True

def avi_to_mov(filePath):
    outputFile = (filePath.rstrip(filePath[-4:]))
    #print("converting avi to mov")
    p = subprocess.Popen("ffmpeg -i {input} {output}.mp4".format(input=filePath, output=outputFile))
    waitMessage()
    p.wait()
    return True

'''def avi_to_mpg(filePath):
    outputFile = (filePath.rstrip(filePath[-4:]))
    #print("converting avi to mpg")
    os.popen("ffmpeg -i {input} {output}.mpg".format(input=filePath, output=outputFile))
    return True'''

def avi_to_wmv(filePath):
    outputFile = (filePath.rstrip(filePath[-4:]))
    #print("converting avi to wmv")
    p = subprocess.Popen("ffmpeg -i {input} {output}.mp4".format(input=filePath, output=outputFile))
    waitMessage()
    p.wait()
    return True

#Pop up messages
def browseMessage():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Please browse for a video to convert")
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

def formatMessage(fileFormat):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("The file format {} is unsupported on this program. Please browse for another file".format(fileFormat))
    msg.setInformativeText("View supported file formats:")
    msg.setDetailedText("The current available file formats are: \n - avi \n \n New Release coming soon.")
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

def typeMessage():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Conversion Error. You tried to convert a video \nwith the same extention. Please choose another \nconversion format. ")
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

def completeMessage(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Conversion Complete")
    msg.setWindowTitle("Complete")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()
    #self.progressBar.setValue(0)

def waitMessage():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("Please wait: \n\nYour video is being converted.\nThis process may take up to 30 Minutes\ndepending on the length of the video.")
    msg.setWindowTitle("Converting Video")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
