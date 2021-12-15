""" Program to reverse the given number """


def reverse_number(x):
    revx = 1
    if x < 0:
        revx = int('-' + str(abs(x))[::-1])
    elif x >= 0:
        revx = int(str(x)[::-1])
    # if revx in range(pow(-2, 31), pow(2, 31)-1): (Can be rewritten as)
    if -2 ** 31 <= revx <= 2 ** 31 - 1:
        return revx
    else:
        return 0


if __name__ == '__main__':
    x = -954321234
    print(reverse_number(x))
