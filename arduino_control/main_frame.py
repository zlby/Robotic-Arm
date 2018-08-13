import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QMainWindow)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn = QPushButton('Button', self)
        btn.resize(btn.sizeHint())
        btn.move(500, 300)

        btn.clicked.connect(self.button_click)

        self.setGeometry(500, 300, 1000, 600)
        self.setWindowTitle('Auto Drug Fetching System')
        self.show()

    def button_click(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())