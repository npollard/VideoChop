# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videochop_gui.ui'
#
# Created: Fri Apr 17 14:38:23 2015
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
        dialog.resize(421, 170)
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
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 50, 221, 41))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.tone_freq = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        self.tone_freq.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tone_freq.setObjectName(_fromUtf8("tone_freq"))
        self.horizontalLayout_4.addWidget(self.tone_freq)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.chop_button = QtGui.QPushButton(dialog)
        self.chop_button.setGeometry(QtCore.QRect(250, 70, 151, 71))
        self.chop_button.setObjectName(_fromUtf8("chop_button"))
        self.horizontalLayoutWidget_5 = QtGui.QWidget(dialog)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 90, 221, 41))
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.tone_freq_2 = QtGui.QLineEdit(self.horizontalLayoutWidget_5)
        self.tone_freq_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tone_freq_2.setObjectName(_fromUtf8("tone_freq_2"))
        self.horizontalLayout_5.addWidget(self.tone_freq_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(dialog)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 130, 221, 41))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_6)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_6.addWidget(self.label_5)
        self.tone_freq_3 = QtGui.QLineEdit(self.horizontalLayoutWidget_6)
        self.tone_freq_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.tone_freq_3.setObjectName(_fromUtf8("tone_freq_3"))
        self.horizontalLayout_6.addWidget(self.tone_freq_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "VideoChop", None))
        self.label_2.setText(_translate("dialog", "Video file:", None))
        self.browse_input.setText(_translate("dialog", "Browse", None))
        self.label_3.setText(_translate("dialog", "Tone Freq #1 (Hz):", None))
        self.tone_freq.setText(_translate("dialog", "50", None))
        self.chop_button.setText(_translate("dialog", "CHOP!", None))
        self.label_4.setText(_translate("dialog", "Tone Freq #2 (Hz):", None))
        self.tone_freq_2.setText(_translate("dialog", "300", None))
        self.label_5.setText(_translate("dialog", "Tone Freq #3 (Hz):", None))
        self.tone_freq_3.setText(_translate("dialog", "20000", None))

