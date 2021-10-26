# Concepts from GeeksforGeeks


def numbers_to_strings(arg1):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(arg1, 'nothing')


# Driver program
if __name__ == "__main__":
    print('Select from 0,1,2: ')
    arg1 = int(input().strip())
    print((numbers_to_strings(arg1)))
