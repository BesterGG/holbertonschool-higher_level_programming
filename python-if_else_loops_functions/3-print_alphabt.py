#!/usr/bin/python3
for i in range(97, 123):
    p = chr(i)
    if i == 113 or i == 101:
        continue
    print("{}".format(p), end="")
