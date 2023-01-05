import cv2
import qrcode

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

# creating the MyGUI class
class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("qrcodegui.ui")
        self.show()

# create main func -> instantiate MyGUI obj -> execute app
def main():
    app = QApplication([])
    MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
