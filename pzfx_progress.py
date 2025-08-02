import os
import re
import time
from lxml import etree
from common import check_file_permissions, check_directory_permissions, get_condition1_from_table_name, get_condition2_from_table_name, get_days
from csv_progress import execute_csv
from initpzfx import initPrismaTaste, initPrisma


def parse_pzfx(pzfx_path):
    tree = etree.parse(pzfx_path)
    root = tree.getroot()
    ns = {'prism': root.nsmap[None]}
    tables = []
    for table_elem in root.xpath('.//prism:Table', namespaces=ns):
        table = {
            'element': table_elem,
            'title': table_elem.findtext('prism:Title', namespaces=ns),
            'x_values': [],
            'y_columns': [],
            'subcolumns': []
        }
        xcol = table_elem.find('.//prism:XColumn', namespaces=ns)
        if xcol is not None:
            xsub = xcol.find('prism:Subcolumn', namespaces=ns)
            if xsub is not None:
                table['x_values'] = [int(x.text) for x in xsub.findall('prism:d', namespaces=ns)]
        for ycol in table_elem.findall('prism:YColumn', namespaces=ns):
            ytitle = ycol.findtext('prism:Title', namespaces=ns)
            subcolumns = ycol.findall('prism:Subcolumn', namespaces=ns)
            table['y_columns'].append({
                'title': ytitle,
                'subcolumns': subcolumns
            })
        tables.append(table)
    return tree, root, tables


def get_fruit_type_from_filename(pzfx_path):
    base = os.path.basename(pzfx_path)
    match = re.match(r'([A-Za-z]+)_', base)
    return match.group(1) if match else None

def extract_fruit_type_from_filename(filename):
    """Extract fruit type from PZFX file name (e.g., 'Apple' from 'Apple_Growth_Condition_Sample.pzfx')."""
    base = os.path.basename(filename)
    match = re.match(r'(\w+)_Growth_Condition', base)
    if match:
        return match.group(1)
    # fallback: use first word before _ or .
    return base.split('_')[0].split('.')[0]

def parse_table_structure(table_title):
    title = table_title.lower().strip()
    if 'in sunny place_good smell' in title and 'many flower' not in title and 'shade' not in title:
        return {
            'columns': [
                    'many fruits_normal color',
                    'many fruits_good color',
                    'a few fruits_normal color',
                    'a few fruits_good color'
                ],
            'subcol_map': {
                'many fruits_normal color': 'A',
                'many fruits_good color': 'B',
                'a few fruits_normal color': 'C',
                'a few fruits_good color': 'D'
            }
        }
    elif 'in sunny place or shade_good smell' in title and 'many flower' not in title:
        return {
            'columns': [
                'many fruits_normal color (in sunny place)',
                'many fruits_normal color (in shade)',
                'many fruits_good color (in sunny place)',
                'many fruits_good color (in shade)'
            ],
            'subcol_map': {
                'many fruits_normal color (in sunny place)': 'A',
                'many fruits_normal color (in shade)': 'B',
                'many fruits_good color (in sunny place)': 'C',
                'many fruits_good color (in shade)': 'D'
            }
        }
    elif 'in sunny place or shade_good smell_many flower' in title:
        return {
            'columns': [
                'many fruits (in sunny place)',
                'many fruits (in shade)',
                'a few fruits (in sunny place)',
                'a few fruits (in shade)'
            ],
            'subcol_map': {
                'many fruits (in sunny place)': 'A',
                'many fruits (in shade)': 'B',
                'a few fruits (in sunny place)': 'C',
                'a few fruits (in shade)': 'D'
            }
        }
    elif 'in sunny place_good smell_many flower' in title:
        return {
            'columns': [
                'many fruits',
                'a few fruits'
            ],
            'subcol_map': {
                'many fruits': 'A',
                'a few fruits': 'B'
            }
        }
    # else:
    # Default: no mapping
    # return {'columns': [], 'subcol_map': {}}

def parse_table_conditions(table_title):
    title = table_title.lower().strip()
    conditions = {
        'location': None,
        'smell': None,
        'other_conditions': []
    }
    if 'in sunny place_good smell' in title and 'many flower' not in title and 'shade' not in title:
        conditions['location'] = 'sunny'
        conditions['smell'] = 'good'
    elif 'in sunny place or shade_good smell' in title and 'many flower' not in title:
        conditions['location'] = 'none'
        conditions['smell'] = 'good'
    elif 'in sunny place or shade_good smell_many flower' in title:
        conditions['location'] = 'none'
        conditions['smell'] = 'good'
        conditions['other_conditions'].append('many flower')
    elif 'in sunny place_good smell_many flower' in title:
        conditions['location'] = 'sunny'
        conditions['smell'] = 'good'
        conditions['other_conditions'].append('many flower')

    return conditions

def get_table_structure_and_conditions(table_title):
    """Get the structure and conditions of the table based on its title."""
    structure = parse_table_structure(table_title)
    conditions = parse_table_conditions(table_title)
    return structure, conditions

def writing_pzfx(inputData, fruitname):
    days, unique_list = get_days(inputData)

    root  = initPrisma()
    ns = {'prism': 'http://graphpad.com/prism/Prism.htm'}

    for table in root.xpath('.//prism:Table', namespaces=ns):
        
        title_elem = table.find('prism:Title', namespaces=ns)
        title = title_elem.text if title_elem is not None else ""
        conditions = get_condition1_from_table_name(title)

        xcol = table.find('.//prism:XColumn', namespaces=ns)
        xadcol = table.find('.//prism:XAdvancedColumn', namespaces=ns)
        xsub = etree.SubElement(xcol, 'Subcolumn')
        xadSub = etree.SubElement(xadcol, 'Subcolumn')
        
        for day in unique_list:
            etree.SubElement(xsub, 'd').text = str(day)
            etree.SubElement(xadSub, 'd').text = str(day)

        ycols = table.findall('.//prism:YColumn', namespaces=ns)

        idx = 0
        for ycol in ycols:
            for i in range(5):
                ysub = etree.SubElement(ycol, 'Subcolumn')
                
            condition = conditions[f"y{idx + 1}"]
            print(f"Processing YColumn {idx + 1} with condition: {condition}")
            for day in unique_list:
                for data in inputData:
                    if data['day'] == day:
                        for table_data in data['data']:
                            print(f"Processing table: {table_data['tableName']} for day {day}")
            idx += 1
            # print(ycol.find('prism:Title', namespaces=ns).text)
    # print(root.xpath('.//prism:Table', namespaces=ns))

    # for table in root.findall('.//Table'):
    #     title_elem = table.find('Title')
    #     title = title_elem.text if title_elem is not None else ""
    #     conditions = get_condition1_from_table_name(title)
    #     print(f"Processing table: {title} with conditions: {conditions}")

    return root



def convert_progress(csv_dir, fruitname, update_progress):
    """Convert CSV data to PZFX format with progress updates."""
    if csv_dir and not check_directory_permissions(csv_dir, 'w'):
        raise PermissionError(f"Permission denied: Cannot write to output directory {csv_dir}")

    # Simulate conversion process
    inputData = execute_csv(csv_dir)

    writing_pzfx(inputData, fruitname)

    

    # process1(inputData, ge)

    # process2(inputData)
    # total_steps = 100
    # for step in range(total_steps):
    #     # Simulate some processing time
    #     time.sleep(0.05)  # Simulating work being done
    #     update_progress(step + 1, total_steps)

    
    # Finalize and save the output PZFX file
    # Here you would implement the actual logic to fill the PZFX with CSV data

