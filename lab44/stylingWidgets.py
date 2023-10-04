import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.btn = qtw.QPushButton('Text in button', self)


		btn_style = """
			border: 20px solid red;
			border-radius: 10px;
			background-color: yellow;
		"""

		self.btn.setStyleSheet(btn_style)








if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	window.show()

	sys.exit(app.exec())
