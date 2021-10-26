""" Program to replace '%' in string A from string B when the first and last characters of strings match. When
they don't match, print -1.
From Numerator coding interview for Data Engineer """


def replacechar(A, B):
	if A[:1] == B[:1] and A[-1:] == B[-1:]:
		charA = A.index('%')
		charB = B.find(A[charA+1:])
		return A[:charA] + B[charA:charB] + A[charA+1:]
	else:
		return -1


if __name__ == '__main__':
	A = 'abc%ijklm'
	B = 'abcdefghijklm'
	print(replacechar(A, B))
