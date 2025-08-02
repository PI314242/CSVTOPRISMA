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

def get_days(day_list):
#    """Analyze the day from a list of strings."""

    days = []
    for day in day_list:
        days.append(day["day"])
    unique_list = list(set(days))
    return days, unique_list

    # days = []
    # for day in day_list:
    #     days.append(day["day"])
    # print(f"Days found: {days}")
    # unique_list = list(set(day_list))
    # print(f"Unique days: {unique_list}")
    # return days,unique_list

# def find_order(day_value, day_list):
#     if day_list.count(day_value) > 1:

def get_condition1_from_table_name(table_name):
    title = table_name.lower().strip()
    conditions = {}
    if 'in sunny place_good smell' in title and 'many flower' not in title and 'shade' not in title:
        conditions = {
            "y1":{
                "table": 'many fruits_normal color',
                "sunny": "sunny",
                "smell": "good",
                'other': []
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': []
            },
            "y3":{
                "table": 'a few fruits_normal color',
                "sunny": "sunny",
                "smell": "good",
                'other': []
            },
            "y4":{
                "table": 'a few fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': []
            },
        }
    elif 'in sunny place or shade_good smell' in title and 'many flower' not in title:
        conditions = {
            "y1":{
                "table": 'many fruits_normal color',
                "sunny": "sunny",
                "smell": "good",
                'other': []
            },
            "y2":{
                "table": 'many fruits_normal color',
                "sunny": "shade",
                "smell": "good",
                'other': []
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': []
            },
            "y4":{
                "table": 'many fruits_good color',
                "sunny": "shade",
                "smell": "good",
                'other': []
            },
        }
    elif 'in sunny place or shade_good smell_many flower' in title:
        conditions = {
            "y1":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["many flower"]
            },
            "y2":{
                "table": 'many fruits',
                "sunny": "shade",
                "smell": "good",
                'other': ["many flower"]
            },
            "y3":{
                "table": 'a few fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["many flower"]
            },
            "y4":{
                "table": 'a few fruits',
                "sunny": "shade",
                "smell": "good",
                'other': ["many flower"]
            },
        }
    elif 'in sunny place_good smell_many flower' in title:
        conditions = {
            "y1":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["many flower"]
            },
            "y2":{
                "table": 'a few fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["many flower"]
            },
        }

    return conditions

def get_condition2_from_table_name(table_name):
    title = table_name.lower().strip()
    conditions = {}
    if 'in sunny place_many flower_normal or good smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y3":{
                "table": 'a few fruits',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y4":{
                "table": 'a few fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
        }
    elif 'in sunny place or shade_many fruits_normal or good smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y3":{
                "table": 'many fruits',
                "sunny": "shade",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y4":{
                "table": 'many fruits',
                "sunny": "shade",
                "smell": "good",
                'other': ["especially tasty"]
            },
        }
    elif 'in the sunny place_fruits number and color_normal smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits_normal color',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y3":{
                "table": 'a few fruits_normal color',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y4":{
                "table": 'a few fruits_good color',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
        }
    elif 'in the sunny place_fruits number and color_good smell_%especially tasty' == title:
        conditions = {
           "y1":{
                "table": 'many fruits_normal color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y3":{
                "table": 'a few fruits_normal color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y4":{
                "table": 'a few fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
        }
    elif 'in the sunny place or the shade_many fruits_normal smell_%especially tasty' == title:
        conditions = {
           "y1":{
                "table": 'many fruits_normal color',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'many fruits_normal color',
                "sunny": "shade",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "normal",
                'other': ["especially tasty"]
            },
            "y4":{
                "table": 'many fruits_good color',
                "sunny": "shade",
                "smell": "normal",
                'other': ["especially tasty"]
            },
        }
    elif 'in the sunny place or the shade_many fruits_good smell_%especially tasty' == title:
        conditions = {
           "y1":{
                "table": 'many fruits_normal color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'many fruits_normal color',
                "sunny": "shade",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y4":{
                "table": 'many fruits_good color',
                "sunny": "shade",
                "smell": "good",
                'other': ["especially tasty"]
            },
        }
    elif 'in the sunny place_fruits size_many fruits good color_good smell_%especially tasty' == title:
        conditions = {
           "y1":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, light"]
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, heavy"]
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, heavy"]
            },
            "y4":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, light"]
            },
        }
    elif 'in the sunny place_fruits size_a few fruits good color_good smell_%especially tasty' == title:
        conditions = {
           "y1":{
                "table": 'a few fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, light"]
            },
            "y2":{
                "table": 'a few fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, heavy"]
            },
            "y3":{
                "table": 'a few fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, heavy"]
            },
            "y4":{
                "table": 'a few fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, light"]
            },
        }
    elif 'in the sunny place_fruits size_many fruits good color_normal or good smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, light"]
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, heavy"]
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, heavy"]
            },
            "y4":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, light"]
            },
        }
    elif 'in the sunny place or the shade_fruit size_many fruits good color_good smell_%especially tasty' == title:
        conditions = {
           "y1":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, light"]
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, heavy"]
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, heavy"]
            },
            "y4":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, light"]
            },
        }
    elif 'coloq_in the sunny place_fruit size_many fruits good color_good smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, light"]
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, heavy"]
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, light"]
            }
        }
    elif 'coloq_in the sunny place_fruit size_a few fruits good color_good smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, light"]
            },
            "y2":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "large, heavy"]
            },
            "y3":{
                "table": 'many fruits_good color',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty", "small, heavy"]
            }
        },
    elif 'coloq_in the sunny place_fruit size_many flowers_good smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'a few fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            }
        },
    elif 'coloq_in the sunny place or the shade_fruit size_many flowers_good smell_%especially tasty' == title:
        conditions = {
            "y1":{
                "table": 'many fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y2":{
                "table": 'a few fruits',
                "sunny": "sunny",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y3":{
                "table": 'many fruits',
                "sunny": "shade",
                "smell": "good",
                'other': ["especially tasty"]
            },
            "y4":{
                "table": 'a few fruits',
                "sunny": "shade",
                "smell": "good",
                'other': ["especially tasty"]
            }
        }

    return conditions
