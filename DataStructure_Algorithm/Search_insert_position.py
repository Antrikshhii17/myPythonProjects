""" Program to find the element if present in the array, if not, get the index where it could have been"""


def searchInsert(nums, target: int) -> int:
    if target not in nums:
        return len([i for i in range(len(nums)) if nums[i] <= target])
    else:
        for i in range(len(nums)):
            if target == nums[i]:
                return i


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 6
    print(searchInsert(nums, target))
