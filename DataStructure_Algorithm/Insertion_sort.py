""" Insertion sort algorithm. Time complexity-
    Worst case = O(n^2) , when the array is in descending order.
    Average case = O(n^2) , when the array is jumbled.
    Best case  = O(n) , when the array is already sorted."""


def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


if __name__ == '__main__':
    list = [3, 1, 8, 5, 9, 13, 10, 6]
    insertionsort(list)
    print(list)
