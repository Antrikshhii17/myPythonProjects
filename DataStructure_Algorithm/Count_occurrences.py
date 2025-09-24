""" Program to count number of occurrences of each element in a list.
    Asked in Precisely interview for Software Engineer-I """


def count_occurrences(ourlist):
    # return dict((i, ourlist.count(i)) for i in ourlist)           # List comprehension approach

    # Dict assignment approach
    # dicx = {}
    # unique_list = set(ourlist)
    # for x in unique_list:
    #     dict[x] = ourlist.count(x)
    
    dicx = {}
    for j in ourlist:
        dicx.__setitem__(j, ourlist.count(j))
    return dicx


if __name__ == '__main__':
    ourlist = [5, 3, 9, 3, 1, 6, 6, 6, 1, 2, 2, 6, 9, 2]
    print(count_occurrences(ourlist))
