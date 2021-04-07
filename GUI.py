from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import sys
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_window_properties()
        self.nonogram_grid, self.vector_x, self.vector_y = self.set_nonogram_skeleton()
        central_widget = self.get_layout()
        self.setCentralWidget(central_widget)
        self.showNormal()

    def set_window_properties(self):
        self.setWindowTitle("Nonogram solver")
        self.setMinimumHeight(600)
        self.setMinimumWidth(600)
  
    def set_nonogram_skeleton(self):
        vector_x, vector_y, nonogram_grid = QTableWidget(), QTableWidget(), QTableWidget()
        
        #vector_y.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        #vector_y.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        vector_y.setColumnCount(3)
        vector_y.setRowCount(3)
        vector_y.horizontalHeader().setDefaultSectionSize(20)
        vector_y.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        vector_y.horizontalHeader().hide()
        vector_y.verticalHeader().setDefaultSectionSize(20)
        vector_y.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        vector_y.verticalHeader().hide()
        vector_y.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding))

        vector_x.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum))
        nonogram_grid.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))

        return nonogram_grid, vector_x, vector_y

    def common_add_row(self, vector):
        column_amount = vector.rowCount()
        vector.insertRow(column_amount)

    def common_add_collumn(self, vector):
        column_amount = vector.columnCount()
        vector.insertColumn(column_amount)

    def common_del_row(self, vector):
        column_amount = vector.rowCount()
        vector.removeRow(column_amount - 1)

    def common_del_collumn(self, vector):
        column_amount = vector.columnCount()
        vector.removeColumn(column_amount - 1)

    def add_y_row(self): self.common_add_row(self.vector_y)
    def add_y_collumn(self): self.common_add_collumn(self.vector_y) 
    def del_y_row(self): self.common_del_row(self.vector_y)
    def del_y_collumn(self): self.common_del_collumn(self.vector_y)

    def add_x_row(self): self.common_add_row(self.vector_x)
    def add_x_collumn(self): self.common_add_collumn(self.vector_x) 
    def del_x_row(self): self.common_del_row(self.vector_x)
    def del_x_collumn(self): self.common_del_collumn(self.vector_x)

    def solve_nonogram(self): pass

    def reset_nonogram(self): 
        self.vector_x.setRowCount(0)
        self.vector_x.setColumnCount(0)
        self.vector_y.setRowCount(0)
        self.vector_y.setColumnCount(0)
        self.nonogram_grid.setRowCount(0)
        self.nonogram_grid.setColumnCount(0)

    def show_next_step(self): pass

    def show_prev_step(self): pass

    def get_button_group(self):
        btn_func = [self.add_y_collumn, self.del_y_collumn, self.add_y_row, self.del_y_row,
                    self.add_x_collumn, self.del_x_collumn, self.add_x_row, self.del_x_row,
                    self.reset_nonogram, self.solve_nonogram, self.show_next_step, self.show_prev_step]
        btn_text = ["Add Y column", "Delete Y column", "Add Y row", "Delete Y row", 
                    "Add X column", "Delete X column", "Add X row", "Delete X row", 
                    "Reset","Solve", "Next step", "Previous step"]
        btn_layout, btn_amount = QVBoxLayout(), len(btn_text) 

        btn_layout.addSpacing(25)
        btn_layout.addWidget(self.get_logo())
        btn_layout.addSpacing(10)  
        
        for index in range(btn_amount):
            if not index % 4: btn_layout.addSpacing(15)

            tmp_btn = QPushButton()
            tmp_btn.setText(btn_text[index])
            tmp_btn.clicked.connect(btn_func[index])
            btn_layout.addWidget(tmp_btn)
            tmp_btn.setDisabled(index > btn_amount - 3)

        btn_layout.addStretch()
        return btn_layout

    def get_logo(self):
        label = QLabel()
        icon = QIcon("crossword.png")
        pixmap = icon.pixmap(QSize(200, 200))
        label.setPixmap(pixmap)
        return label

    def get_layout(self,):
        widget_wrap = QWidget()
        layout_main, layout_center, layout_left = QHBoxLayout(widget_wrap), QVBoxLayout(),  QVBoxLayout()
        btn_layout = self.get_button_group()

        layout_main.addLayout(layout_left)
        layout_main.addLayout(layout_center)
        layout_main.addSpacing(10)
        layout_main.addLayout(btn_layout)

        layout_left.addWidget(QLabel("Solving vector Y"))
        layout_left.addWidget(self.vector_y)

        layout_center.addWidget(QLabel("Solving vector X"))
        layout_center.addWidget(self.vector_x)
        layout_center.addWidget(QLabel("Nonogram view"))
        layout_center.addWidget(self.nonogram_grid)
      
        return widget_wrap
    

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())