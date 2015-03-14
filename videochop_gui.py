# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videochop_gui.ui'
#
# Created: Fri Mar 13 21:00:39 2015
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
        dialog.resize(423, 105)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dialog.setWindowIcon(icon)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 401, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.input_path = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.input_path.setObjectName(_fromUtf8("input_path"))
        self.horizontalLayout.addWidget(self.input_path)
        self.browse_input = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.browse_input.setObjectName(_fromUtf8("browse_input"))
        self.horizontalLayout.addWidget(self.browse_input)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 401, 41))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.tone_freq = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        self.tone_freq.setMaximumSize(QtCore.QSize(40, 16777215))
        self.tone_freq.setObjectName(_fromUtf8("tone_freq"))
        self.horizontalLayout_4.addWidget(self.tone_freq)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.chop_button = QtGui.QPushButton(self.horizontalLayoutWidget_4)
        self.chop_button.setObjectName(_fromUtf8("chop_button"))
        self.horizontalLayout_4.addWidget(self.chop_button)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "VideoChop", None))
        self.label_2.setText(_translate("dialog", "Video file:", None))
        self.browse_input.setText(_translate("dialog", "Browse", None))
        self.label_3.setText(_translate("dialog", "Tone Freq (Hz):", None))
        self.tone_freq.setText(_translate("dialog", "300", None))
        self.chop_button.setText(_translate("dialog", "CHOP!", None))

