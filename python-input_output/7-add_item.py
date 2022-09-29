#!/usr/bin/python3
"""
Write a script that adds all arguments to a python list,
and then save them to a file.
"""
import sys
import os.path

SV = __import__('5-save_to_json_file').save_to_json_file
LD = __import__('6-load_from_json_file').load_from_json_file

f = "add_item.json"
ld = LD(f) if os.path.exists(f) else []
for i in sys.argv:
    f.append(i)
SV(ld, f)
