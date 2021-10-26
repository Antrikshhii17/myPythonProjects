""" Bubble sort. Time complexity-
    Worst case = O(n^2) , when the array is in descending order.
    Average case = O(n^2) , when the array is jumbled.
    Best case = O(n) , when the array is already sorted. """


def bubblesort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


if __name__ == '__main__':
    list = [31, 9, 5, 10, 6, 12, 8, 1]
    bubblesort(list)
    print(list)
