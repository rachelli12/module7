"""
Program name: sort_and_search_list.py
Author: Rachel Li
Last date modified: 06/19/2020

The purpose of this program is to search and sort list of items
and print the index of the item
and print the sorted list.
"""
fruit_list = ['apple', 'orange', 'pear', 'grape', 'peach', 'strawberry', 'mango']

def search_list(fruit_item):
    """
    use reST style
    :param fruit_item: this represents object being searched
    "param fruit_list: this represents list where object is searched
    :return: the index of the object
    :raises keyError: raises an exception
    """
    try:
        # search_list.index()
        y = fruit_list.index(fruit_item)
        # return the index of the object in the list
        return y
    except ValueError as err:
        # return -1 if the item is not found
        print('-1', err)
        raise ValueError

def sort_list():
    """
    use reST style

    :raises keyError: raises an exception
    """
    #sort the list
    fruit_list.sort()
    #do not need return value because the sort function already returns the sorted list

if __name__=='__main__':
    search_fruit = search_list('peach')
    print(search_fruit)

    sort_list()
    print(fruit_list)






