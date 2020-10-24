# Filename: calculator.py 

'''simple calculator with PyQt5 '''

import sys

#import QApplication and all the required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QHBoxLayout

#Create an instance of QApplication
#sys.argv passes command line arguments. If the application doesnt accept CL args, then you can do an empty list like
#QApplication([])

app = QApplication(sys.argv)

#Create an instance of the applications GUI

window = QWidget()
window.setWindowTitle('Box layout')
layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_)
