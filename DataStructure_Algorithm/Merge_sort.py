""" Merge sort algorithm. Time complexity-
    Worst case = O(n*log n). Average case = O(n*log n). Best case = O(n*log n) """


def mergesort(mylist):
    if len(mylist) > 1:
        r = len(mylist)//2
        l1 = mylist[:r]
        l2 = mylist[r:]

        mergesort(l1)
        mergesort(l2)

        i = j = k = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                mylist[k] = l1[i]
                i += 1
            else:
                mylist[k] = l2[j]
                j += 1
            k += 1
        while i < len(l1):
            mylist[k] = l1[i]
            i += 1
            k += 1
        while j < len(l2):
            mylist[k] = l2[j]
            j += 1
            k += 1


if __name__ == '__main__':
    mylist = [12, 2, 19, 35, 47, 6, 1]
    mergesort(mylist)
    print(mylist)
