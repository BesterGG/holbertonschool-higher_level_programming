#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    my_list = my_list[::-1]
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))

    # #!/usr/bin/python3
# def print_reversed_list_integer(my_list=[]):
#     for i in reversed(my_list):
#         print("{:d}".format(i))
# #!/usr/bin/python3

# C Style 8)
# def print_reversed_list_integer(my_list=[]):
#     Len = len(my_list)
#     for i in range (int(Len/2)):
#         n = my_list[i]
#         my_list[i] = my_list[Len - i - 1]
#         my_list[Len - i - 1] = n
#     print("{:d}".format(my_list[0]))
