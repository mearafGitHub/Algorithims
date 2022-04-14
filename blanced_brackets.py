import math
import os
#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# more efficent
def valid_brackets(brackets):
    store = []
    brackets_table = {')': '(', ']': '[', '}': '{'}
    for b in brackets:
        if b in brackets_table:
            if store and store[-1] == brackets_table[b]:
                store.pop()
            else:
                return False
        else:
            store.append(b)
    if not store:
        return True
    else:
        return False

def isBalanced(brackets):
    # Write your code here
    n = 0
    while (len(brackets) != n):
        n = len(brackets);
        brackets = brackets.replace('()', '');
        brackets = brackets.replace('[]', '');
        brackets = brackets.replace('{}', '');

    if (len(brackets) == 0):
        return "YES"
    else:
        return "NO"
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     t = int(input().strip())
#
#     for t_itr in range(t):
#         s = input()
#         s = '()[]{}'
#         result = isBalanced(s)
#
#         fptr.write(result + '\n')
#
#     fptr.close()

s = '()[]{}'
print(valid_brackets(s))


