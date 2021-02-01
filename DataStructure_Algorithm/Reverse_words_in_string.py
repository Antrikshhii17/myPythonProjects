# Program for reversing words in a string (Geeksforgeeks practice question)


def reverse(s):           # Approach(1)- Using for loop

    # Splitting using '.' and converting to list
    splitted = list(s.split('.'))
    splitted2 = ''

    # Iterating over list items and appending with '.'
    for i in splitted:
        splitted2 = i + '.' + splitted2

    return splitted2[:-1]  # Eliminating last character because it has an additional '.'


# This is our string to be used
s = 'i.like.this.program.very.much'

result = reverse(s)
print(result)

"""
def reverse(s):           # Approach(2)- Reversing the list

    # Splitting using '.' and converting to list
    splitted = list(s.split('.'))

    # Using reverse function to reverse the list
    splitted.reverse()

    # Joining our list items again with '.'
    return '.'.join(splitted)


# This is our string to be used
s = 'i.like.this.program.very.much'

result = reverse(s)
print(result)
"""