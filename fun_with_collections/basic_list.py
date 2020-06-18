def get_input():
    #ask user input of number
    number = input("Please enter a number: ")
    #return a string
    return number


def make_list():
    #declare a list variable
    list = []
    # try and cast to numeric type
    try:
        # for loop with range
        # for something in range(start, end)
        for l in range (0,3):
            # call get_input(), set to variable
            x = int(get_input())
            # append to list declared
            list.append(x)
        return list #return list
    except ValueError as err :
        print("ValueError",err)
        raise ValueError
        #raise an exception if cannot convert


if __name__=='__main__':
    a = make_list()
    print(a)
