class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def inorder(root, k):
            if not root:
                return
            inorder(root.left, k)
            if k > 0:
                result.append(root.val)
                k -= 1
            if k == 0:
                return
            inorder(root.right, k)
            return
        inorder(root, k)
        return result[k-1]
