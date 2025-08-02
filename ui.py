import os

from PyQt6.QtWidgets import (
     QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QProgressBar, QHBoxLayout, QLineEdit
)

from common import check_file_permissions
from pzfx_progress import convert_progress

# ----------------- GUI -----------------
class AutoFillerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PZFX AutoFiller")
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.csv_dir = ""

        self.csv_label = QLabel("CSV Data Directory: (not selected)")

        self.progress = QProgressBar()
        self.progress.setValue(0)

        layout.addWidget(self.csv_label)
        layout.addWidget(self.progress)

        btn_layout = QHBoxLayout()
        self.btn_csv = QPushButton("Select CSV Directory")
        self.fruitname = QLineEdit("Enter Fruit Name")
        self.btn_run = QPushButton("Run AutoFill")

        btn_layout.addWidget(self.btn_csv)
        btn_layout.addStretch()
        btn_layout.addWidget(self.fruitname)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_run)
        layout.addLayout(btn_layout)

        self.btn_csv.clicked.connect(self.select_csv)
        # self.fruitname.textChanged.connect(lambda: setattr(self, 'fruitname', self.fruitname.text()))
        self.btn_run.clicked.connect(self.run_autofill)

    # def select_pzfx(self):
    #     file, _ = QFileDialog.getOpenFileName(self, "Select PZFX File", "", "PZFX Files (*.pzfx)")
    #     if file:
    #         self.pzfx_path = file
    #         self.pzfx_label.setText(f"PZFX File: {file}")

    def select_csv(self):
        dir = QFileDialog.getExistingDirectory(self, "Select CSV Data Directory")
        if dir:
            self.csv_dir = dir
            self.csv_label.setText(f"CSV Data Directory: {dir}")

    # def select_output(self):
    #     file, _ = QFileDialog.getSaveFileName(self, "Select Output PZFX File", "", "PZFX Files (*.pzfx)")
    #     if file:
    #         self.output_path = file
    #         self.output_label.setText(f"Output PZFX File: {file}")

    def update_progress(self, filled, total):
        self.progress.setMaximum(total)
        self.progress.setValue(filled)

    def run_autofill(self):
        if  not self.csv_dir or not self.fruitname.text().strip(" "):
            QMessageBox.warning(self, "Missing Input", "Please select all input/output files.")
            return
        
        self.progress.setValue(0)
        
        try:
            # Check if files exist and are accessible
            if not os.path.exists(self.csv_dir):
                QMessageBox.critical(self, "Directory Error", f"CSV directory not found:\n{self.csv_dir}")
                return
            

            # fruit_type = extract_fruit_type_from_filename(self.pzfx_path)
            # print(f"[Info] Using fruit_type: '{fruit_type}' from PZFX file name: {self.pzfx_path}")
            
            # fill_pzfx(self.pzfx_path, self.csv_dir, self.output_path, self.update_progress)
            convert_progress(self.csv_dir, self.fruitname.text(), self.update_progress)


            QMessageBox.information(self, "Success", f"Filled PZFX saved to:\n{self.csv_dir}")

        except PermissionError as e:    
            QMessageBox.critical(self, "Permission Error", 
                                f"Permission denied:\n{str(e)}\n\n"
                                "Please ensure:\n"
                                "- Files are not open in other applications\n"
                                "- You have write permissions to the output directory\n"
                                "- Try running as administrator if needed")
        except FileNotFoundError as e:
            QMessageBox.critical(self, "File Error", f"File not found:\n{str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred:\n{str(e)}")
