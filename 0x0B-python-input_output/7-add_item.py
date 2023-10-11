#!/usr/bin/python3
"""cript that adds all arguments to a Python list,
and then save them to a file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argulist = list(sys.argv[1:])

try:
    o_data = load_from_json_file('add_item.json')
except Exception:
    o_data = []
o_data.extend(argulist)
save_to_json_file(o_data, "add_item.json")
