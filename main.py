import sys
from lxml import etree
import tempfile
from ui import AutoFillerGUI  # Assuming AutoFillerGUI is defined in ui.py
from PyQt6.QtWidgets import QApplication


def main():
    try:
        # Test basic functionality
        print("Starting PZFX AutoFiller...")
        print("Checking basic permissions...")
        
        # Test if we can create a temporary file
        try:
            test_file = tempfile.NamedTemporaryFile(delete=True)
            test_file.close()
            print("✓ Basic file operations working")
        except Exception as e:
            print(f"⚠ Warning: File operations may be limited: {e}")
        
        app = QApplication(sys.argv)
        gui = AutoFillerGUI()
        gui.show()
        print("✓ GUI started successfully")
        sys.exit(app.exec())
    except Exception as e:
        print(f"Critical error starting application: {e}")
        print("Please ensure you have proper permissions and try running as administrator if needed.")
        input("Press Enter to exit...") 

# ----------------- Entry Point -----------------
if __name__ == '__main__':
            main()
