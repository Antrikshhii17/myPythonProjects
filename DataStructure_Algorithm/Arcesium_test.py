# Coding test


def maximumProduct(inputArray):
    answer = 1
    for i in inputArray:
        answer = answer * i
    return int(answer % 1000000007)


if __name__ == '__main__':
    inputArray_count = int(input().strip())
    inputArray = []

    for _ in range(inputArray_count):
        inputArray_item = int(input().strip())
        inputArray.append(inputArray_item)

    result = maximumProduct(inputArray)
    print(result)
