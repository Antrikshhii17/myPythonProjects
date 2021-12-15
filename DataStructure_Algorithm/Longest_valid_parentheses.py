""" Program to find the length of longest valid parentheses using stack data structure """


def isValid(string):
    stack = [-1]
    res = 0
    for idx, i in enumerate(string):
        if i == '(':
            stack.append(idx)
        else:
            stack.pop()
            if not stack:
                stack.append(idx)
            else:
                res = max(res, idx-stack[-1])
    return res


if __name__ == '__main__':
    string = '()(()()()()'
    print(isValid(string))
