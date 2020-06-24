from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

class Window(QMainWindow):

    def UI(self): 
        self.combo_box = QComboBox(self)  
        self.combo_box.setGeometry(225, 150, 150, 30) 
        sports_list = ["Football", "Cricket", "Basketball", "Golf"] 
        self.combo_box.setEditable(True) 
        self.combo_box.addItems(sports_list) 
        combobox_model = QtGui.QStandardItemModel(0, 1) 
        add_item = QtGui.QStandardItem("Add model") 
        combobox_model.appendRow(add_item) 
        self.combo_box.setModel(combobox_model) 
        get_modelname = self.combo_box.model() 
        label = QLabel("Model = " + str(get_modelname), self)  
        label.setGeometry(100, 100, 800, 30) 
  
    def __init__(self): 
        super().__init__()  
        self.setWindowTitle("Python ComboBox Model")  
        self.setGeometry(100, 100, 600, 400) 
        self.UI()   
        self.show() 

App = QApplication(sys.argv) 
window = Window() 
sys.exit(App.exec()) 