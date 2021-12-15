""" Linear search algorithm to find an element from a list
    Time complexity- O(n) """


def findelem(list, elem):
    for i in range(len(list)):
        if list[i] == elem:
            return i
    return -1


if __name__ == '__main__':
    list = [10, 4, 9, 34, 1, 21, 59]
    elem = 10                            # Input element to be found.
    result = findelem(list, elem)
    if result == -1:
        print('The element is missing.')
    else:
        print('The target element is at index:', result)
