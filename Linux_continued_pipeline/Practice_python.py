# Filter even numbers
number = [10, 25, 30, 49, 50, 63, 70, 87, 91]


def check_even(num):
    if num % 2 == 0:
        return True

    return False


even_nums_iter = filter(check_even, number)

even_num_list = list(even_nums_iter)
print(even_num_list)

# Using the lambda function
even = filter(lambda x: x % 2 == 0, number)
even_list = list(even)
print(even_list)


# ####################################### Map function ##############################################
numbers = [64, 23, 59, 72, 60, 17, 94, 29, 2]


def convert_to_usd(numb):
    return numb * 73


converted = map(convert_to_usd, numbers)
converted_list = list(converted)
print(converted_list)
