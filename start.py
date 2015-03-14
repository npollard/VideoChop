import sys
from chop import chopify
from os.path import isfile
from PyQt4 import QtCore, QtGui
from videochop_gui import Ui_dialog

class StartQT4(QtGui.QMainWindow):
 def __init__(self, parent=None):
  QtGui.QWidget.__init__(self, parent)
  self.ui = Ui_dialog()
  self.ui.setupUi(self)
  QtCore.QObject.connect(self.ui.browse_input, QtCore.SIGNAL("clicked()"), self.browseInput)
  QtCore.QObject.connect(self.ui.chop_button, QtCore.SIGNAL("clicked()"), self.chop)

 def browseInput(self):
  fd = QtGui.QFileDialog(self)
  self.filename = fd.getOpenFileName()
  if isfile(self.filename):
   self.ui.input_path.setText(self.filename)

 

 def chop(self):
  videoPath = self.ui.input_path.text()
  freq = self.ui.tone_freq.text()
  print "chopify(" + videoPath + ", " + freq + ")"
  chopify(videoPath, int(freq))

if __name__ == "__main__":
 app = QtGui.QApplication(sys.argv)
 myapp = StartQT4()
 myapp.show()
 sys.exit(app.exec_())
