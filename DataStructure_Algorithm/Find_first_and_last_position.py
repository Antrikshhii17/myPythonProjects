""" Program to find first and last position of the element in a sorted array"""


def searchRange(nums, target):
    if target not in nums:
        return [-1, -1]
    idx1 = nums.index(target)
    nums.reverse()
    idx2 = len(nums) - 1 - nums.index(target)
    return [idx1, idx2]


if __name__ == '__main__':
    nums = [2, 4, 7, 7, 9, 13, 18]
    target = 7
    print(searchRange(nums, target))
