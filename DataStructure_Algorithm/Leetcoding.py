# Two sum


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}
#         for i, value in enumerate(nums):  # 1
#             remaining = target - nums[i]  # 2
#
#             if remaining in seen:  # 3
#                 return [i, seen[remaining]]  # 4
#             else:
#                 seen[value] = i


dict1={"a":10,"b":2,"c":3}
str1=""
for i in dict1:
  str1=str1+str(dict1[i])+" "
  str2=str1[:-1]
print(str2[::-1])


def my_func(num):
  data = [0]
  for i in range(1, num+1):
    data.append(data[i >> 1] + int(i & 1))
  return data


num = 6
print(my_func(num))

# def my_func(nums):
#   count = 0
#   for i, j in enumerate(nums):
#     if i > count:
#       return False
#     count = max(count, i + j)
#   return True


# if __name__ == "__main__":
#   print(my_func([3, 2, 1, 0, 4]))

circle_areas = [3.54773, 5.57778, 4.00014, 59.24241, 34.01344, 32.01013]

result = list(map(round, circle_areas, range(1, 3)))
print(result)