import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')

		# using inline style- not good
		self.btn1 = qtw.QPushButton('Button 1')
		btn_style = """
			border: 5px solid red;
			border-radius: 10px;
			background-color: yellow;
			padding-top:10px;
			padding-bottom:10px;
		"""
		self.btn1.setStyleSheet(btn_style)

		# using external css file - best variant
		self.btn2 = qtw.QPushButton('Button 2')
		self.btn3 = qtw.QPushButton('Button 3')
		self.btn3.setObjectName('btn3')
		self.btn4=qtw.QPushButton('Button 4')

		self.label1 = qtw.QLabel('label1')
		self.label2 = qtw.QLabel('label2')
		self.label3 = qtw.QLabel('label3')

		group1 = qtw.QGroupBox()
		horLayout = qtw.QHBoxLayout()
		horLayout.addWidget(self.label1)
		horLayout.addWidget(self.btn4)
		horLayout.addWidget(self.label2)
		group1.setLayout(horLayout)

		self.mainLayout = qtw.QVBoxLayout()
		self.mainLayout.addWidget(self.btn1)
		self.mainLayout.addWidget(self.btn2)
		self.mainLayout.addWidget(self.btn3)
		self.mainLayout.addWidget(group1)
		self.mainLayout.addWidget(self.label3)

		self.setLayout(self.mainLayout)

		### apply main stylesheet:
		with open('./main.css') as f:
			style = f.read()

		self.setStyleSheet(style)











if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	window.show()

	sys.exit(app.exec())
