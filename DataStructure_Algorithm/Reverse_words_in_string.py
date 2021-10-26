# Program for reversing words in a string (Geeksforgeeks practice question)


def reverse(string):
    res = ''
    for i in list(string.split('.')):
        res = ''.join(i + '.' + res)
    return res[:-1]  # Eliminating the additional '.' in the end


if __name__ == '__main__':
    string = 'much.very.program.this.like.i'
    result = reverse(string)
    print(result)
