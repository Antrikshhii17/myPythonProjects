# Coding test


def maximumProduct(inputarray):
    max = inputarray[0]
    for i in inputarray:
        if i > max:
            max = i
    prod = 1
    for j in inputarray:
        prod *= j
    return prod * max


if __name__ == '__main__':
    inputarray_count = int(input().strip())
    inputarray = []
    for _ in range(inputarray_count):
        inputarray_item = int(input().strip())
        inputarray.append(inputarray_item)
    result = maximumProduct(inputarray)
    print(result)
