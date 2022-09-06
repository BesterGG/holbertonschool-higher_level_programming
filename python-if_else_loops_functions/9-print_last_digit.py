#!/usr/bin/python3
def print_last_digit(number):
    ld = abs(number) % 10
    print("{}".format(str(ld), end=""))
    return ld
