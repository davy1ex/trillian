import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Trillian')
        self.resize(500, 320)

        self.setStyleSheet("QWidget {background-image: url(2341.jpg) }")


        self.text_field = QTextBrowser(self)


        self.input_line = QLineEdit(self)


        vbox = QVBoxLayout(self)
        vbox.addStretch(1)

        vbox.addWidget(self.text_field)
        vbox.addWidget(self.input_line)

        vbox.addStretch(1)
        self.setLayout(vbox)

        self.text_field.resize(350, 170)
        self.input_line.resize(350, 170)


        # # self.setLayout(hbox)
        # vbox.setAlignment(QtCore.Qt.AlignCenter)
        # central_frame = QFrame(self) # .setFrameShape(QFrame.StyledPanel)
        # central_frame.move(self.pos())
        # bottom = QFrame(self)




        # self.input_line(300, 22)


        self.show()



if '__main__' == __name__:
    app = QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec_())

