""" Program to get only duplicates from a list of numbers.
Asked in Numerator interview for Data Engineer """


def getdups(nums):
    seen = set()
    res = []
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
        else:
            res.append(nums[i])
    return list(set(res))


if __name__ == '__main__':
    nums = [3, 8, 5, 9, 2, 2, 2, 2, 7, 8, 2, 7, 7, 7, 7]
    print(getdups(nums))
