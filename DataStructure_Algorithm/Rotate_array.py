""" Program to rotate array K times in anti-clockwise direction if Dir = 'A' or in clockwise direction if
the Dir = 'C'. A is the input array.
 From Numerator coding interview for Data Engineer """


def rotateKtimes(N, A, Dir, K):
	for v in range(K):
		rotateArray(N, A, Dir)


def rotateArray(N, A, Dir):  # Rotating the array one time
	first, last = A[0], A[-1]
	if Dir == 'C':
		for i in range(N - 1, -1, -1):
			A[i] = A[i - 1]
		A[0] = last
	else:  # When Dir = 'A'
		for j in range(N - 1):
			A[j] = A[j + 1]
		A[-1] = first


def printArray(A, N):
	for i in range(N):
		print('%d' % A[i], end=' ')


if __name__ == '__main__':
	A = [1, 2, 3, 4, 5]
	N, Dir, K = 5, 'C', 2
	rotateKtimes(N, A, Dir, K)
	printArray(A, N)
