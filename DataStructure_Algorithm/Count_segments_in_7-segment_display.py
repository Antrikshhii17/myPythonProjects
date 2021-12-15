""" Program to find the count of segments used in 7-segment display of the given number.
    Example(1)- Input: '495'        Example(2)- Input: '123'        Example(3)- Input: '11'
               Output: 15                      Output: 12                      Output: 4
    Explanation- I'm storing the segment count of each number in dictionary, then adding them in a variable 'sum' """


def segmentdisplay(number):
    segments = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
    summ = 0
    for i in number:
        summ += segments[i]
    return summ


if __name__ == '__main__':
    number = '495'
    print(segmentdisplay(number))
