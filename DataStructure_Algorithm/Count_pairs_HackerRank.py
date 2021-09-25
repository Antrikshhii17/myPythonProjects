# Comment out one part when executing the code.
# Using normal function :-      PART(1)


def sockmerchant(n, ar):
    count1 = []
    for i in set(ar):
        count1.append(ar.count(i)//2)
    return sum(count1)


if __name__ == '__main__':
    n = int(input().strip())  # Driver code
    ar = list(map(int, input().rstrip().split(',')))
    result = sockmerchant(n, ar)
    print(result)

'''Explanation : 
Here, the set() function makes the array distinct and sorted. Next, each number is divided by 2 with 
floor divison and the count is taken. Next, sum gives the pair from the counted list'''

# Using list comprehension :-     PART(2)


# def sockmerchant(n, ar):
#     return sum([ar.count(i)//2 for i in set(ar)])
#
#
# if __name__ == '__main__':
#     n = int(input().strip())  # Driver code
#     ar = list(map(int, input().rstrip().split(',')))
#     result = sockmerchant(n, ar)
#     print(result)
