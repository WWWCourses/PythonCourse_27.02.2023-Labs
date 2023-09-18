class QApplication(QGuiApplication):
	# Public Functions
	def __init__(self):
		# Properties (attributes)
		self.autoSipEnabled = True


	def autoSipEnabled(self):
		return self.autoSipEnabled




app = QApplication()

# read autoSipEnabled:
print(self.autoSipEnabled())

# set autoSipEnabled
app.setAutoSipEnabled(False)