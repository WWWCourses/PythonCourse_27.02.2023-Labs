import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)


		self.createGridLayout()
		self.addMainLayout()
		self.addHLayout()
		# self.addVLayout()


		self.setWindowTitle('Layout Demo')
		self.show();

	def addMainLayout(self):
		leOutput = qtw.QLineEdit()

		mainLayout = qtw.QVBoxLayout()

		mainLayout.addWidget(leOutput)
		mainLayout.addLayout(self.gridLayout)

		self.setLayout(mainLayout)


	def createGridLayout(self):
		# create child widgets
		btnBackspace = qtw.QPushButton('Backspace')
		btnClear = qtw.QPushButton('Clear')
		btnClearAll = qtw.QPushButton('ClearAll')

		# create GridLayout
		self.gridLayout=qtw.QGridLayout()

		# create 1st row
		self.gridLayout.addWidget(btnBackspace,0,0,1,2)
		self.gridLayout.addWidget(btnClear,0,2,1,2)
		self.gridLayout.addWidget(btnClearAll,0,4,1,2)

		# create 2nd row
		rowBtnNames = ['MC', '7', '8', '9', '%', 'Sqrt']
		for i,name in enumerate(rowBtnNames):
			btn = qtw.QPushButton(name)
			self.gridLayout.addWidget(btn,1,i)


	def addVLayout(self):
		# create child widgets
		btn1 = qtw.QPushButton('btn1')
		btn2 = qtw.QPushButton('btn2')
		btn3 = qtw.QPushButton('btn3')

		# create VLayout
		VLayout = qtw.QVBoxLayout()
		self.setLayout(VLayout)

		# add child to layout
		VLayout.addWidget(btn3)
		VLayout.addWidget(btn2)
		VLayout.addWidget(btn1)

	def addHLayout(self):
		# create child widgets
		btn1 = qtw.QPushButton('btn1')
		btn2 = qtw.QPushButton('btn2')
		btn3 = qtw.QPushButton('btn3')

		# create HLayout
		hLayout = qtw.QHBoxLayout(self)

		# add child to layout
		hLayout.addWidget(btn3)
		hLayout.addWidget(btn2)
		hLayout.addWidget(btn1)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())
