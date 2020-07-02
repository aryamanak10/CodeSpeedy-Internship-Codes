from PyQt5.QtWidgets import * 
from PyQt5 import QtGui 
from PyQt5.QtGui import * 
import sys

class Window_ComboBox(QMainWindow):

    def UI(self1): 
        self1.combo_box = QComboBox(self1)  
        self1.combo_box.setGeometry(225, 150, 150, 30) 
        sports_list = ["Football", "Cricket", "Basketball", "Golf"] 
        self1.combo_box.setEditable(True) 
        self1.combo_box.addItems(sports_list) 
        combobox_model = QtGui.QStandardItemModel(0, 1) 
        add_item = QtGui.QStandardItem("Add model") 
        combobox_model.appendRow(add_item) 
        self1.combo_box.setModel(combobox_model) 
        get_modelname = self1.combo_box.model() 
        label = QLabel("Model = " + str(get_modelname), self1)  
        label.setGeometry(100, 100, 800, 30) 
  
    def __init__(self1): 
        super().__init__()  
        self1.setWindowTitle("Python ComboBox Model")  
        self1.setGeometry(100, 100, 600, 400) 
        self1.UI()   
        self1.show() 

App = QApplication(sys.argv) 
window = Window_ComboBox() 
sys.exit(App.exec()) 