import sys
import typing
from PyQt6 import QtGui, QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('App')
		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)

		self.addMenuBar()
		self.addToolbar()
		self.addActions()
		# self.addDock()
		self.addStatusBar()


	def addMenuBar(self):
		# get the menu bar
		self.menubar = self.menuBar()

		# add menu items
		self.file_menu = self.menubar.addMenu('&File')
		self.edit_menu = self.menubar.addMenu('&Edit')
		self.help_menu = self.menubar.addMenu('&Help')

	def addToolbar(self):
		toolbar = self.addToolBar('File')

		toolbar.setMovable(True)
		toolbar.setFloatable(False)

		# for Qt6:
		toolbar.setAllowedAreas(
			qtc.Qt.ToolBarArea.TopToolBarArea |
			qtc.Qt.ToolBarArea.BottomToolBarArea
		)

		self.toolbar = toolbar


		# standardIcon = self.style().standardIcon(getattr(qtw.QStyle.StandardPixmap,'SP_DialogHelpButton'))

	def addDock(self):
		dock = qtw.QDockWidget("Replace")
		# TODO: update for PyQt6:
		self.addDockWidget(qtc.Qt.LeftDockWidgetArea, dock)

		# set dock widget to move and float (but not closeable)
		dock.setFeatures(
		# for pyqt6
			qtw.QDockWidget.DockWidgetFeature.DockWidgetMovable |
			qtw.QDockWidget.DockWidgetFeature.DockWidgetFloatable
		)

	def addActions(self):
		# add actions
		open_action = self.file_menu.addAction('Open', lambda : print('Open'))
		save_action = self.file_menu.addAction('Save', lambda : print('Save'))

		# add separator
		self.file_menu.addSeparator()

		quit_action = self.file_menu.addAction('Quit', self.close)

		undo_action = self.edit_menu.addAction('Undo', self.textedit.undo)

		# create a QAction manually
		redo_action = qtg.QAction('Redo', self)
		redo_action.triggered.connect(self.textedit.redo)

		# Actions, which opens custom dialog
		self.edit_menu.addAction(redo_action)
		# self.edit_menu.addAction('Set Font…', self.setFont)
		# self.edit_menu.addAction('Settings…', self.showSettings)

	def addStatusBar(self):
		#  create status bar widget and atach it to main window:
		self.status_bar = qtw.QStatusBar()
		self.setStatusBar(self.status_bar)

		# show temporary message for 3 second:
		self.status_bar.showMessage('Welcome to My Text Editor',5000)

		charcount_label = qtw.QLabel("chars: 0")
		self.textedit.textChanged.connect(
		lambda: charcount_label.setText( "chars: " + str(len(self.textedit.toPlainText())) )
		)
		self.status_bar.addPermanentWidget(charcount_label)

	def addCustomActions(self):
		self.help_action = qtg.QAction(
			self.style().standardIcon(getattr(qtw.QStyle.StandardPixmap,'SP_DialogHelpButton')),
			'Help',
			self  # important to pass the parent!
		)

		# add signal
		self.help_action.triggered.connect(lambda : qtw.QMessageBox.information(self,'Not Implemented','Sorry, no help yet!'))

		self.toolbar.addAction(self.help_action)


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	window.show()

	sys.exit(app.exec())
