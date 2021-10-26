""" Selection sort algorithm. Time complexity-
    Worst case = O(n^2). Average case = O(n^2). Best case = O(n^2) """


def selectionsort(nums):
    for i in range(len(nums)):
        minidx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minidx]:
                minidx = j
        nums[i], nums[minidx] = nums[minidx], nums[i]


if __name__ == '__main__':
    nums = [19, 56, 2, 72, 1, 29, 9, 3]
    selectionsort(nums)
    print(nums)
