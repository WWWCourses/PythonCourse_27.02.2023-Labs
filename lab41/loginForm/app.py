import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('Login Form')
		# self.setGeometry(0, 0, 50, 50)

		# Generate main widgets
		leUserName = qtw.QLineEdit()
		leUserPass = qtw.QLineEdit()
		leUserPass.setEchoMode(qtw.QLineEdit.EchoMode.Password)
		btnOK = qtw.QPushButton('OK')
		btnCancel = qtw.QPushButton('Cancel')


		# Create layouts
		formLayout=qtw.QFormLayout()
		buttonsLayout = qtw.QHBoxLayout()


		# layout widgets:
		formLayout.addRow('UserName', leUserName)
		formLayout.addRow('UserPass', leUserPass)

		buttonsLayout.addWidget(btnOK)
		buttonsLayout.addWidget(btnCancel)

		formLayout.addRow(buttonsLayout)


		# attach Form layout to self:
		self.setLayout(formLayout)

















if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
