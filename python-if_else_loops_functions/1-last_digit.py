#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = abs(number) % 10
else:
    lastdigit = number % 10
if number == 0:
    str1 = " and is 0"
elif lastdigit > 5:
    str1 = " and is greater than 5"
elif lastdigit < 6:
    str1 = " and is less than 6 and not 0"
print ("Last digit of {} is {}{}".format(number, lastdigit, str1))
