""" Find the smallest element and its index in a list """


def myalgo(list):
    temp = 0
    min = list[0]
    for idx, i in enumerate(list):
        if i < min:
            min, temp = i, idx
    return min, temp


if __name__ == '__main__':
    list = [62, 59, 49, 30, 25, 20, 17]
    result = myalgo(list)
    print(f'The smallest element is: %d at the index: %d' % result)
