""" Program to validate the parenthesis with correct order """


def validparenthesis(string) -> bool:
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []
    for i in string:
        if i in brackets:
            if stack and stack[-1] == brackets[i]:
                stack.pop()
        else:
            stack.append(i)
    return True if not stack else False


if __name__ == '__main__':
    string = '[](){}('
    print(validparenthesis(string))
