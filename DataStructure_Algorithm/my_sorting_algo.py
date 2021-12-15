""" Program for sorting algorithm based on the subtraction of numbers """


def diffsort(numbers):
    numbers[numbers.index(min(numbers))], numbers[0] = numbers[0], min(numbers)
    for i in range(len(numbers)-2):
        #for j in range(i+1, len(numbers)-1):
        if numbers[i] - numbers[i+1] > numbers[i] - numbers[i+2]:
            numbers[i] = numbers[i+1]
        #i += 1
# INCOMPLETE
    return numbers


if __name__ == '__main__':
    numbers = [2, 3, 4, 5, 6, 1]
    print(diffsort(numbers))
