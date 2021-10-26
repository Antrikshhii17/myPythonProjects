""" Q- slice the tuple from index 1 to 3 and join them using comma as string """

tup = (1, 3, 5, 6, 9, 4, 2)

result = ','.join(map(str, tup[1:4]))
print(result)
