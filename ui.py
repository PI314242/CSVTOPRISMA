import os

from PyQt6.QtWidgets import (
     QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QMessageBox, QProgressBar, QHBoxLayout
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

        self.pzfx_path = ""
        self.csv_dir = ""
        self.output_path = ""

        self.pzfx_label = QLabel("PZFX File: (not selected)")
        self.csv_label = QLabel("CSV Data Directory: (not selected)")
        self.output_label = QLabel("Output PZFX File: (not selected)")
        self.progress = QProgressBar()
        self.progress.setValue(0)

        layout.addWidget(self.pzfx_label)
        layout.addWidget(self.csv_label)
        layout.addWidget(self.output_label)
        layout.addWidget(self.progress)

        btn_layout = QHBoxLayout()
        self.btn_pzfx = QPushButton("Select PZFX File")
        self.btn_csv = QPushButton("Select CSV Directory")
        self.btn_output = QPushButton("Select Output File")
        self.btn_run = QPushButton("Run AutoFill")
        btn_layout.addWidget(self.btn_pzfx)
        btn_layout.addWidget(self.btn_csv)
        btn_layout.addWidget(self.btn_output)
        btn_layout.addWidget(self.btn_run)
        layout.addLayout(btn_layout)

        self.btn_pzfx.clicked.connect(self.select_pzfx)
        self.btn_csv.clicked.connect(self.select_csv)
        self.btn_output.clicked.connect(self.select_output)
        self.btn_run.clicked.connect(self.run_autofill)

    def select_pzfx(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select PZFX File", "", "PZFX Files (*.pzfx)")
        if file:
            self.pzfx_path = file
            self.pzfx_label.setText(f"PZFX File: {file}")

    def select_csv(self):
        dir = QFileDialog.getExistingDirectory(self, "Select CSV Data Directory")
        if dir:
            self.csv_dir = dir
            self.csv_label.setText(f"CSV Data Directory: {dir}")

    def select_output(self):
        file, _ = QFileDialog.getSaveFileName(self, "Select Output PZFX File", "", "PZFX Files (*.pzfx)")
        if file:
            self.output_path = file
            self.output_label.setText(f"Output PZFX File: {file}")

    def update_progress(self, filled, total):
        self.progress.setMaximum(total)
        self.progress.setValue(filled)

    def run_autofill(self):
        if not self.pzfx_path or not self.csv_dir or not self.output_path:
            QMessageBox.warning(self, "Missing Input", "Please select all input/output files.")
            return
        
        # Reset progress bar
        self.progress.setValue(0)
        
        try:
            # Check if files exist and are accessible
            if not os.path.exists(self.pzfx_path):
                QMessageBox.critical(self, "File Error", f"PZFX file not found:\n{self.pzfx_path}")
                return
                
            if not os.path.exists(self.csv_dir):
                QMessageBox.critical(self, "Directory Error", f"CSV directory not found:\n{self.csv_dir}")
                return
            
            # Check permissions
            if not check_file_permissions(self.pzfx_path, 'r'):
                QMessageBox.critical(self, "Permission Error", 
                                   f"Permission denied reading PZFX file:\n{self.pzfx_path}\n\n"
                                   "Please ensure the file is not open in another application.")
                return
            
            output_dir = os.path.dirname(self.output_path)
            if output_dir and not os.path.exists(output_dir):
                try:
                    os.makedirs(output_dir, exist_ok=True)
                except PermissionError:
                    QMessageBox.critical(self, "Permission Error", 
                                       f"Permission denied creating output directory:\n{output_dir}")
                    return
            

            # fruit_type = extract_fruit_type_from_filename(self.pzfx_path)
            # print(f"[Info] Using fruit_type: '{fruit_type}' from PZFX file name: {self.pzfx_path}")
            
            # fill_pzfx(self.pzfx_path, self.csv_dir, self.output_path, self.update_progress)

            convert_progress(self.pzfx_path, self.csv_dir, self.output_path, self.update_progress)


            QMessageBox.information(self, "Success", f"Filled PZFX saved to:\n{self.output_path}")
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
