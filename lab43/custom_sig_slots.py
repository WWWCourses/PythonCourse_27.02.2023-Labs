import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):
	# signals
	sig_submit = qtc.pyqtSignal(int)


	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create UI widgets and layouts
		self.setupUI()

		# signals
		self.btnSubmit.clicked.connect(self.btnSubmitClicked)
		self.leUserName.textChanged.connect(self.leUserNameTextChangedHandler)

	# TODO: finsih example
	def btnSubmitClicked(self, *args):
			print('btnSubmitClicked')
			print(args)
			x = 1
			self.sig_submit.emit(x)

	@qtc.pyqtSlot(bool)
	def btnSubmitClickedHandler(self,*args,**kwargs):
		print('btnSubmit was clicked')
		print(f'args: {args}')
		print(f'kwargs: {kwargs}')

	@qtc.pyqtSlot(str)
	def leUserNameTextChangedHandler(self,*args,**kwargs):
		print('leUserName text was changed')
		print(f'args: {args}')
		print(f'kwargs: {kwargs}')


	def setupUI(self):
		self.setWindowTitle('Lab43')

		self.leUserName = qtw.QLineEdit()
		self.leUserName.setPlaceholderText('Enter user name')

		self.btnSubmit = qtw.QPushButton('Submit')
		self.btnSubmit.setCheckable(True)


		mainLayout = qtw.QVBoxLayout()
		mainLayout.addWidget(self.leUserName)
		mainLayout.addWidget(self.btnSubmit)
		self.setLayout(mainLayout)



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()
	window.show()

	sys.exit(app.exec())
