# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')

        def traversal(root):
            nonlocal maximum
            if not root:
                return 0
            
            left = max(0,traversal(root.left))
            right = max(0,traversal(root.right))
            path = left + right + root.val
            maximum = max(maximum,path)
            return root.val + max(left,right)

        traversal(root)
        return maximum 