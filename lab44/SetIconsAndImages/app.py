import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('App')


		self.lImage = qtw.QLabel()
		self.main_layout = qtw.QVBoxLayout()
		self.main_layout.addWidget(self.lImage)


		self.mainWidget = qtw.QWidget()
		self.setCentralWidget(self.mainWidget)
		self.mainWidget.setLayout(self.main_layout)

		img = qtg.QPixmap('./images/medicine-8287535_1280.jpg')
		self.lImage.setPixmap(img)
		self.lImage.resize(300,200)

		self.setWindowIcon(qtg.QIcon('./icons/calculator.png'))

		self.iconsDemo()

	def iconsDemo(self):
		themeIcon = qtg.QIcon.fromTheme("accessories-calculator")
		self.btnThemeIcon = qtw.QPushButton('btnThemeIcon')
		self.btnThemeIcon.setIcon(themeIcon)
		self.main_layout.addWidget(self.btnThemeIcon)

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	window.show()

	sys.exit(app.exec())
