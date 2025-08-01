import os

def check_file_permissions(file_path, mode='r'):
    """Check if file can be accessed with given mode."""
    try:
        if mode == 'r':
            with open(file_path, 'r') as f:
                pass
        elif mode == 'w':
            with open(file_path, 'w') as f:
                pass
        return True
    except PermissionError:
        return False
    except Exception:
        return False

def check_directory_permissions(dir_path, mode='r'):
    """Check if directory can be accessed with given mode."""
    try:
        if mode == 'r':
            # Try to list directory contents
            os.listdir(dir_path)
        elif mode == 'w':
            # Try to create a test file
            test_file = os.path.join(dir_path, '.test_permissions')
            with open(test_file, 'w') as f:
                f.write('test')
            os.remove(test_file)
        return True
    except PermissionError:
        return False
    except Exception:
        return False

def is_file_in_use(file_path):
    """Check if a file is currently being used by another process."""
    try:
        # Try to open the file in exclusive mode
        with open(file_path, 'r+b') as f:
            pass
        return False  # File is not in use
    except PermissionError as e:
        error_msg = str(e)
        if "being used by another process" in error_msg or "WinError 32" in error_msg:
            return True  # File is in use
        else:
            return False  # Other permission error
    except Exception:
        return False  # File doesn't exist or other error
