# #!/usr/bin/python3
# """ Write a """
# import sys
# import os.path

# SV = __import__('5-save_to_json_file').save_to_json_file
# LD = __import__('6-load_from_json_file').load_from_json_file

# fd = "add_item.json"
# ld = LD(fd) if os.path.exists(fd) else []
# for i in sys.argv:
#     fd.append(i)
# SV(ld, fd)

#!/usr/bin/python3
""" load, add, save """
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fp = "add_item.json"
ls = load_from_json_file(fp) if os.path.exists(fp) else []

for i in sys.argv:
    ls.append(i)
save_to_json_file(ls, fp)