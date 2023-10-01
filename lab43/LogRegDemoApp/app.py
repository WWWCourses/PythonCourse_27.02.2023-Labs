import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

from registrationForm import FormWindow
from db import DB

class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.db = DB(user='test', password='test1234', db='pyqt_users_db')

		# self.db.create_user_table()

		self.btnRegistration = qtw.QPushButton('Registration')
		self.btnLogIn = qtw.QPushButton('LogIn')

		ml = qtw.QHBoxLayout()
		ml.addWidget(self.btnRegistration)
		ml.addWidget(self.btnLogIn)

		self.setLayout(ml)
		self.setWindowTitle('')


		self.btnRegistration.clicked.connect(self.onRegistration)

	def onRegistration(self):
		self.form = FormWindow()
		self.form.show()
		self.form.submit.connect(self.onRegistrationSubmit)


	def onRegistrationSubmit(self, *args, **kwargs):
		print('onRegistrationSubmit')
		print(f'args: {args}')


		self.db.insert_row(args[0], args[1])

	# TODO (HW): implement Login Form and its functionality

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	window.show()

	sys.exit(app.exec())
