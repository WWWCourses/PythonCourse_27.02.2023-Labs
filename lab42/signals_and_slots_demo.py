import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.setGeometry(600, 400, 300, 300)

		self.setupUI()

		# when the button is clicked => do ClickedAction
		self.counter = 1
		self.btnClick.clicked.connect( self.clickedAction )
		self.btnClick.pressed.connect( self.lOutput.setText )


		#
		self.btnSubmit.clicked.connect(self.userNameSubmitAction)

		self.leUserName.textEdited.connect(print )

	def setupUI(self):
		self.leUserName = qtw.QLineEdit()
		self.btnSubmit = qtw.QPushButton('Submit')
		userNameLayout = qtw.QHBoxLayout()
		userNameLayout.addWidget(self.leUserName)
		userNameLayout.addWidget(self.btnSubmit)

		self.lOutput = qtw.QLabel('Output')
		self.btnClick = qtw.QPushButton('Click me')
		self.btnCheckBox = qtw.QCheckBox()

		buttonsLayout = qtw.QHBoxLayout()
		buttonsLayout.addWidget(self.btnClick)
		buttonsLayout.addWidget(self.btnCheckBox)



		mainLayout = qtw.QVBoxLayout()
		mainLayout.addLayout(userNameLayout)
		mainLayout.addWidget(self.lOutput)
		mainLayout.addLayout(buttonsLayout)
		self.setLayout(mainLayout)

	def userNameTextEditAction(self):
		# user_name = self.leUserName.text()
		pass


	def userNameSubmitAction(self):
		user_name =  self.leUserName.text()
		self.lOutput.setText(user_name)

	def pressedAction(self):
		print(f'Pressed {self.counter} times')


	def clickedAction(self,*args):
		if self.counter<5:
			print(f'Clicked {self.counter} times')
			print(f'args: {args}')
		else:
			self.btnClick.clicked.disconnect()

			# self.lOutput.setText('Change')
		self.counter+=1





if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
