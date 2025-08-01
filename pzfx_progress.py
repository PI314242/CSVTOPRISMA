import os
import re
import time
import xml.etree.ElementTree as etree
from common import check_file_permissions, check_directory_permissions
from csv_progress import execute_csv

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



def convert_progress(pzfx_path, csv_dir, output_path, update_progress):
    """Convert CSV data to PZFX format with progress updates."""
    if not os.path.exists(pzfx_path):
        raise FileNotFoundError(f"PZFX file not found: {pzfx_path}")
        
    if not check_file_permissions(pzfx_path, 'r'):
        raise PermissionError(f"Permission denied: Cannot read PZFX file {pzfx_path}")
    
    # Check output directory permissions
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except PermissionError:
            raise PermissionError(f"Permission denied: Cannot create output directory {output_dir}")
    
    if output_dir and not check_directory_permissions(output_dir, 'w'):
        raise PermissionError(f"Permission denied: Cannot write to output directory {output_dir}")

    # Simulate conversion process
    
    # total_steps = 100
    # for step in range(total_steps):
    #     # Simulate some processing time
    #     time.sleep(0.05)  # Simulating work being done
    #     update_progress(step + 1, total_steps)

    execute_csv(csv_dir)
    
    # Finalize and save the output PZFX file
    # Here you would implement the actual logic to fill the PZFX with CSV data
