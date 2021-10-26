""" Program to return length of the last word in a string """


def lengthlast(string):
    return len(string.strip().split(' ')[-1])


if __name__ == '__main__':
    string = 'This is a sample string1296949585   string2     '
    result = lengthlast(string)
    print(result)
