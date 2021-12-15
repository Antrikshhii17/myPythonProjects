""" Program to output the combination of least number of currency notes to give a specific sum amount """


def smallest_notes(sum1) -> dict:
    notes = (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
    result = {}
    for i in notes:
        result[i] = sum1 // i
        sum1 = sum1 % i
    return result


if __name__ == '__main__':
    sum1 = 5378
    print(smallest_notes(sum1))
