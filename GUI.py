jbhntr861@gmail.com
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QTextEdit, QVBoxLayout, QHBoxLayout

class RemoteAccessTool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load the style sheet
        with open('style.qss') as f:
            self.setStyleSheet(f.read())

        # Create the layout
        layout = QGridLayout()

        # Add the buttons
        buttons = ["Read SMS", "Send SMS", "Make Phone Call", "Get Contacts", "Uninstall Apps", "Install Apps", "Use Browser", "Keylogger"]
        for i, text in enumerate(buttons):
            button = QPushButton(text)
            layout.addWidget(button, i//2, i%2)
            button.clicked.connect(getattr(self, text.replace(" ", "").lower()))

        # Set the layout and window properties
        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Remote Access Tool")
        self.show()

    # Define the button functions
    def readSMS(self):
        print("Reading SMS...")

    def sendSMS(self):
        print("Sending SMS...")

    def makePhoneCall(self):
        print("Making a phone call...")

    def getContacts(self):
        print("Getting contacts...")

    def uninstallApps(self):
        print("Uninstalling apps...")

    def installApps(self):
        print("Installing apps...")

    def useBrowser(self):
        print("Using the web browser...")

    def keylogger(self):
        self.keylogger_window = Keylogger()
        self.keylogger_window.show()

class Keylogger(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load the style sheet
        with open('style.qss') as f:
            self.setStyleSheet(f.read())

        # Create the layout
        layout = QVBoxLayout()

        # Add the title label
        title_label = QLabel("Keylogger")
        title_label.setStyleSheet("font-size: 20px;")
        layout.addWidget(title_label)

        # Add the text box
        self.text = QTextEdit()
        self.text.setPlaceholderText("Enter text here...")
        layout.addWidget(self.text)

        # Add the start and stop buttons
        start_button = QPushButton("Start Keylogger")
        stop_button = QPushButton("Stop Keylogger")
        button_layout = QHBoxLayout()
        button_layout.addWidget(start_button)
        button_layout.addWidget(stop_button)
        layout.addLayout(button_layout)

        # Set the layout and window properties
        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Keylogger")

    # Function to get text from the text box
    def get_text(self):
        return self.text.toPlainText()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setStyle("fusion") # Set the style to the Fusion style
    ex = RemoteAccessTool()
    sys.exit(app.exec_())
