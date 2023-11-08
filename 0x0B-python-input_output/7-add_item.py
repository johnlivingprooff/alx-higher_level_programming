#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file:"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    current_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    current_list = []

args = sys.argv[1:]
current_list.extend(args)

save_to_json_file(current_list, 'add_item.json')
