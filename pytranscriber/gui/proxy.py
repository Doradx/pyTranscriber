# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\proxy.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 120)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonNone = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonNone.sizePolicy().hasHeightForWidth())
        self.radioButtonNone.setSizePolicy(sizePolicy)
        self.radioButtonNone.setChecked(True)
        self.radioButtonNone.setObjectName("radioButtonNone")
        self.verticalLayout_2.addWidget(self.radioButtonNone)
        self.radioButtonHTTP = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonHTTP.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonHTTP.sizePolicy().hasHeightForWidth())
        self.radioButtonHTTP.setSizePolicy(sizePolicy)
        self.radioButtonHTTP.setObjectName("radioButtonHTTP")
        self.verticalLayout_2.addWidget(self.radioButtonHTTP)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditHttpProxy = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditHttpProxy.setToolTip("")
        self.lineEditHttpProxy.setStatusTip("")
        self.lineEditHttpProxy.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.lineEditHttpProxy.setObjectName("lineEditHttpProxy")
        self.gridLayout.addWidget(self.lineEditHttpProxy, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButtonTest = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonTest.setEnabled(True)
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.gridLayout.addWidget(self.pushButtonTest, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.radioButtonNone.clicked['bool'].connect(self.lineEditHttpProxy.setDisabled)
        self.radioButtonNone.clicked['bool'].connect(self.pushButtonTest.setDisabled)
        self.radioButtonHTTP.clicked['bool'].connect(self.pushButtonTest.setEnabled)
        self.radioButtonHTTP.clicked['bool'].connect(self.lineEditHttpProxy.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Proxy setting"))
        self.radioButtonNone.setText(_translate("Dialog", "None"))
        self.radioButtonHTTP.setText(_translate("Dialog", "HTTP"))
        self.lineEditHttpProxy.setPlaceholderText(_translate("Dialog", "http://127.0.0.1:1080"))
        self.label.setText(_translate("Dialog", "URL:"))
        self.pushButtonTest.setText(_translate("Dialog", "Test"))