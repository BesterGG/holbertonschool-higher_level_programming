#!/usr/bin/python3
""" load, add, save """
import sys
import os.path
SV = __import__('5-save_to_json_file').save_to_json_file
LD = __import__('6-load_from_json_file').load_from_json_file

fd = "add_item.json"
ld = LD(fd) if os.path.exists(fd) else []

for i in range(1, len(sys.argv)):
    ld.append(i)
SV(ld, fd)
