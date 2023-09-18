import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from ui.Ui_login_form import Ui_Form

class MainWindow(qtw.QWidget, Ui_Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# --------------------------- your code starts here -------------------------- #
		self.setupUi(self)
		# ---------------------------- your code ends here --------------------------- #
		self.show();

  # ------------------------ create your methods here -------------------------- #

if __name__ == '__main__':
  app = qtw.QApplication(sys.argv);

  window = MainWindow()

  sys.exit(app.exec())