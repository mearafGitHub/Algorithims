"""

We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.

Example
Operations are requested as follows:

add ed
add eddie
add edward
find ed
add edwina
find edw
find a
Three  operations include the names 'ed', 'eddie', and 'edward'. Next,  matches all  names. Note that it matches and counts the entire name 'ed'. Next, add 'edwina' and then find 'edw'.  names match: 'edward' and 'edwina'. In the final operation, there are  names that start with 'a'. Return the array .

Function Description

Complete the contacts function below.

contacts has the following parameters:

string queries[n]: the operations to perform
Returns

int[]: the results of each find operation
Input Format

The first line contains a single integer, , the number of operations to perform (the size of ).
Each of the following  lines contains a string, .

Constraints

 and  contain lowercase English letters only.
The input does not have any duplicate  for the  operation.
Sample Input

STDIN           Function
-----           --------
4               queries[] size n = 4
add hack        queries = ['add hack', 'add hackerrank', 'find hac', 'find hak']
add hackerrank
find hac
find hak
Sample Output

2
0
Explanation

Add a contact named hack.
Add a contact named hackerrank.
Find the number of contact names beginning with hac. Both name start with hac, add  to the return array.
Find the number of contact names beginning with hak. neither name starts with hak, add  to the return array.


"""


class node2(dict):
    __slots__ = ['numDescendants']

    def __init__(self):
        self.numDescendants = 0

    def addChild(self, child):  # child is a character
        self[child] = node2()
        self.numDescendants += 1

    def getNumDescendants(self):
        return self.numDescendants

    def incNumDescendants(self):
        self.numDescendants += 1


class Contacts():
    def __init__(self):
        self.root = node2()

    def addName(self, name):
        def Helper(currNode, suffix):
            if len(suffix) == 0:
                currNode.addChild('')  # termination character
            else:
                if suffix[0] in currNode:
                    currNode.incNumDescendants()
                    Helper(currNode[suffix[0]], suffix[1:])
                else:
                    currNode.addChild(suffix[0])
                    Helper(currNode[suffix[0]], suffix[1:])

        currNode = self.root
        Helper(currNode, name)

    def findName(self, prefix):
        def findPrefix(currNode, prefix):
            if len(prefix) == 0:
                return currNode
            else:
                if prefix[0] in currNode:
                    return findPrefix(currNode[prefix[0]], prefix[1:])
                return -1

        nameLoc = findPrefix(self.root, prefix)
        if nameLoc == -1:
            print(0)
        else:
            print(nameLoc.getNumDescendants())
        return


a = Contacts()
numLines = int(input())
while numLines > 0:
    command = input()
    if command[0] == 'a':
        a.addName(command[4:])
    elif command[0] == 'f':
        a.findName(command[5:])
    numLines -= 1