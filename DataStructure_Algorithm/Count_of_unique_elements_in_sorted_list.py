""" Program to return count of unique elements in a sorted list containing multiple duplicates """


def getuniquecount(list):
	uniques = 1
	for i in range(len(list)-1):
		if list[i] != list[i+1]:
			list[uniques] = list[i+1]
			uniques += 1
	return uniques


if __name__ == '__main__':
	list = [1, 4, 4, 5, 7, 7, 7, 12, 12, 18, 18, 18, 18]
	result = getuniquecount(list)
	print(result)
