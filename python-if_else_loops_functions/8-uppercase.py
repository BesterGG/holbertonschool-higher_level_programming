#!/usr/bin/python3
from ast import Str

#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            result += chr(ord(c) - 32)
        else:
            result += chr(ord(c))
    print("{}".format(result))
