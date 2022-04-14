def balancedBrackets(string):
    stack = []
    for s in string:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        elif s:
            b = stack.pop()
            if b == '{' and s != '}':
                return False
            elif b == '[' and s != ']':
                return False
            elif b == '(' and s != ')':
                return False

    if stack:
        return False

    return True


print(balancedBrackets('{[()]}'))
