# Program for binary search in a sorted array


def binarysearch(nums, left, right, x):
    # (Here nums is the array and x is the element to look for)
    while left <= right:
        mid = left + (right - left) // 2

        # If element is present in the middle itself
        if x == nums[mid]:
            return mid

        # If element is present on the left side
        elif x < nums[mid]:
            right = mid - 1

        # If element is present on the right side
        else:
            left = mid + 1

    # If the element is not present in the array
    return -1


nums1 = [2,3,7,15,45,59,88,93,95]
x1 = 3
result = binarysearch(nums1,0,len(nums1)-1,x1)
print(result)
