import sys

# 1. import needed QtWidgets classes
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel

# 2. the main app instance for our application.
app = QApplication(sys.argv)


# 3. Create Qt widget, which will be our main window.
# QWidget([parent=None[, f=Qt.WindowFlags()]])
window = QWidget()

# Add child widjets
user_name_lbl = QLabel('User name: ', parent=window)
# user_name = QLineEdit(parent=window)

# 4. show the window
window.show()


# 5. Start the event loop
app.exec()