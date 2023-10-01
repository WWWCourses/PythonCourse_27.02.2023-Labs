import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class FormWindow(qtw.QWidget):
	submit = qtc.pyqtSignal(str,str)
	def __init__(self , *args, **kwargs):


		super().__init__(*args, **kwargs)
		self.setWindowTitle('Registration')


		self.leUserName = qtw.QLineEdit()
		self.lePass = qtw.QLineEdit()
		self.lePass.setEchoMode(qtw.QLineEdit.EchoMode.Password)
		self.btn_submit = qtw.QPushButton('Submit')

		ml = qtw.QFormLayout()
		ml.addRow('User name: ', self.leUserName)
		ml.addRow('Password: ', self.lePass)
		# TODO: add vertical spacer
		ml.addRow(self.btn_submit)

		self.setLayout(ml)

		# signals
		self.btn_submit.clicked.connect(self.btnSubmitHandler)

	def btnSubmitHandler(self):
		user_name = self.leUserName.text()
		password = self.lePass.text()
		self.submit.emit(user_name,password)
		self.close()




if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	form = FormWindow()

	form.show()

	sys.exit(app.exec())
