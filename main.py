from PySide6.QtWidgets import QMainWindow, QApplication
from interface import Ui_MainWindow
from bot import bot_whatsapp
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.exitButton.clicked.connect(exit)
        self.startButton.clicked.connect(self.start_bot)

    def start_bot(self):
        self.close()
        bot_whatsapp()
        exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()
