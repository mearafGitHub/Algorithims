"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below.

isBalanced has the following parameter(s):

string s: a string of brackets
Returns

string: either YES or NO
Input Format

The first line contains a single integer , the number of strings.
Each of the next  lines contains a single string , a sequence of brackets.

Constraints

, where  is the length of the sequence.
All chracters in the sequences ∈ { {, }, (, ), [, ] }.
Output Format

For each string, return YES or NO.

Sample Input

STDIN           Function
-----           --------
3               n = 3
{[()]}          first s = '{[()]}'
{[(])}          second s = '{[(])}'
{{[[(())]]}}    third s ='{{[[(())]]}}'
Sample Output

YES
NO
YES
Explanation

The string {[()]} meets both criteria for being a balanced string.
The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
The string {{[[(())]]}} meets both criteria for being a balanced string.

"""


def check():
    stack = []
    s = input()
    for c in s:
        # print(c)
        if c == '(':
            stack.append(0);
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return -1
        elif c == '[':
            stack.append(2)
        elif c == ']':
            if len(stack) > 0 and stack[-1] == 2:
                stack.pop()
            else:
                return -1
        if c == '{':
            stack.append(4)
        elif c == '}':
            if len(stack) > 0 and stack[-1] == 4:
                stack.pop()
            else:
                return -1

    if len(stack) == 0:
        return 0
    else:
        return -1


def solve():
    t = int(input())
    for i in range(0, t):
        if check() == 0:
            print("YES")
        else:
            print("NO")


solve()



#  Java sol

"""
public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int numQueries = Integer.parseInt(br.readLine());
    HashMap<String, Integer> map = new HashMap<String, Integer>();

    for (int i = 0; i < numQueries; i++){
        String[] data = br.readLine().split(" ");

        if (data[0].equals("add")){
            for (int j = 1; j <= data[1].length(); j++){
                String sub = data[1].substring(0, j);
                if (map.get(sub) == null){
                    map.put(sub, 1);
                } else {
                    map.put(sub, map.get(sub) + 1);
                }
            }
        } else { //query matches
            if (map.get(data[1]) == null){
                System.out.println(0);
            } else {
                System.out.println(map.get(data[1]));
            }

        }
    }
}
"""