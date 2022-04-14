def getHeight(self, root):
    # Write your code here
    leftHeight = 0
    rightHeight = 0
    if (root.left):
        leftHeight = self.getHeight(root.left) + 1

    if (root.right):
        rightHeight = self.getHeight(root.right) + 1

    if (leftHeight > rightHeight):
        return leftHeight
    else:
        return rightHeight


def topView(root):
    #Write your code here
    traker = [root]
    while len(traker) > 0:
        next = traker.pop(0)
        print(next, end=" ")
        if next.right:
            traker.append(next.right)

