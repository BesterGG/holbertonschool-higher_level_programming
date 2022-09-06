def print_last_digit(number):
    if number < 0:
        return ("{}".format(abs(number)%10))
    else:
        return ("{}".format(number%10))