""" Program to print common prefix in all strings in a list. If the prefix is not found, print nothing.
From Leetcode """


def commonprefix(strs):
	if not strs:
		return ''
	minx = min(strs, key=len)
	for idx, i in enumerate(minx):
		for j in strs:
			if i != j[idx]:
				return minx[:idx]
	return minx


	# output = ''  # This is another algorithm taken from discussion section.
	# for v in zip(*strs):
	# 	if (v[0],) * len(v) == v:
	# 		output += v[0]
	# 	else:
	# 		break
	# return output


if __name__ == '__main__':
	strs = ['total', 'totally', 't', 'tobacco']
	print(commonprefix(strs))
