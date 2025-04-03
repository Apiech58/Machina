# Form implementation generated from reading ui file 'photoeditpage.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from functiontile import FunctionTile


class Photoedit(object):
    def __init__(self,Form):



        Form.setObjectName("Form")
        Form.resize(795, 501)
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 561, 491))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 489))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 561, 491))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.PhotoELayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.PhotoELayout.setContentsMargins(0, 0, 0, 0)
        self.PhotoELayout.setObjectName("PhotoELayout")
        self.PhotoELoader = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.PhotoELoader.setObjectName("PhotoELoader")
        self.PhotoELayout.addWidget(self.PhotoELoader)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.ControllsCombo = QtWidgets.QComboBox(parent=Form)
        self.ControllsCombo.setGeometry(QtCore.QRect(570, 10, 221, 24))
        self.ControllsCombo.setObjectName("ControllsCombo")
        self.ControllsCombo.addItem("Test1")
        self.ControllsCombo.addItem("Test2")
        self.ControllsCombo.addItem("Test3")
        self.ControllsCombo.addItem("Test4")
        self.ControllsCombo.setCurrentIndex(0)
        self.ControllsCombo.currentTextChanged.connect(lambda:self.GetIndex())
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(570, 40, 221, 461))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 219, 459))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 211, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ControllsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ControllsLayout.setContentsMargins(0, 0, 0, 0)
        self.ControllsLayout.setObjectName("ControllsLayout")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def GetIndex(self):
        print(self.ControllsCombo.currentIndex())
        self.addControls()
        
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.PhotoELoader.setText(_translate("Form", "Loading Photo..."))
    def setActivePhoto(self,path):
        photoE = QtGui.QPixmap(path)
        self.PhotoELoader.pixmap(photoE)
    def addControls(self):
        self.ControllsLayout.addWidget(FunctionTile("HEHE"))
        self.verticalLayoutWidget.findChild(QtWidgets.QSlider,"HEHE",QtCore.Qt.FindChildOption.FindChildrenRecursively).valueChanged.connect(lambda:print("YIPPEE"))
        self.ControllsLayout.addWidget(FunctionTile("HAA"))
        self.verticalLayoutWidget.findChild(QtWidgets.QSlider,"HAA",QtCore.Qt.FindChildOption.FindChildrenRecursively).valueChanged.connect(lambda:print("YES"))



