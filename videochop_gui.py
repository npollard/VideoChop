# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videochop_gui.ui'
#
# Created: Fri Mar 13 20:14:57 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(421, 183)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        self.horizontalLayoutWidget = QtGui.QWidget(dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 391, 112))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.input_path = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.input_path.setObjectName(_fromUtf8("input_path"))
        self.verticalLayout.addWidget(self.input_path)
        self.o = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.o.setObjectName(_fromUtf8("o"))
        self.verticalLayout.addWidget(self.o)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tone_freq = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.tone_freq.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tone_freq.setObjectName(_fromUtf8("tone_freq"))
        self.horizontalLayout_3.addWidget(self.tone_freq)
        spacerItem = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.browse_input = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.browse_input.setObjectName(_fromUtf8("browse_input"))
        self.verticalLayout_2.addWidget(self.browse_input)
        self.browse_output = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.browse_output.setObjectName(_fromUtf8("browse_output"))
        self.verticalLayout_2.addWidget(self.browse_output)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 120, 371, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.quit_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.quit_button.setObjectName(_fromUtf8("quit_button"))
        self.horizontalLayout.addWidget(self.quit_button)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.chop_button = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.chop_button.setObjectName(_fromUtf8("chop_button"))
        self.horizontalLayout.addWidget(self.chop_button)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "VideoChop", None))
        self.label_2.setText(_translate("dialog", "Video file:", None))
        self.label.setText(_translate("dialog", "Output directory:", None))
        self.label_3.setText(_translate("dialog", "Tone Freq (Hz):", None))
        self.tone_freq.setText(_translate("dialog", "300", None))
        self.browse_input.setText(_translate("dialog", "Browse", None))
        self.browse_output.setText(_translate("dialog", "Browse", None))
        self.quit_button.setText(_translate("dialog", "Quit", None))
        self.chop_button.setText(_translate("dialog", "CHOP!", None))

