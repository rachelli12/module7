import array as arr

number_list = [1.2, 4.6, 7.8, 4.3, 5.9, 4.8, 9.1]
n = arr.array('d',[1.2, 4.6, 7.8, 4.3, 5.9, 4.8, 9.1])

def search_array(number_item):
    try:
    # array.index(x)
        y = n.index(number_item)
    #return the index of the object in the list
        return y
    #or -1 if the item is not found
    except ValueError as err:
        print('-1', err)
        raise ValueError
    pass

def sort_array():
    #sort the list
    #list.sort(x)
    number_list.sort()
    #no return statement
    #number_lst.sort() already returns the sorted list


if __name__ == '__main__':
    search_number = search_array(5.9)
    print(search_number)

    sort_array()
    print(number_list)
