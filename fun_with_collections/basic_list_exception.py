"""
Program name: basic_list_exception.py
Author: Rachel Li
Last date modified: 06/18/2020

The purpose of this program is to get input
and print user input as list
"""
def get_input():
    """
    use reST style.

    :param number: this represents user input for number
    :return: user input with number
    """
    #ask user input of number
    number = input("Please enter a number: ")
    #return a string
    return number


def make_list():
    """
    use reST style.

    :param number: this calls function get_input as integer
    :return: list with number
    :raises keyError: raises an exception
    """
    #declare a list variable
    list = []
    # try and cast to numeric type
    try:
        # for loop with range
        # for something in range(start, end)
        for l in range (0,3):
            # call get_input(), set to variable
            x = int(get_input())
            list.append(x)
            # append to list declared
            if x < 1 or x > 50:
                raise ValueError
            else:
                continue
    except ValueError as err :
        print("ValueError",err)
        raise ValueError
        #raise an exception if cannot convert
      # return list
    return list

if __name__=='__main__':
    print(make_list())
