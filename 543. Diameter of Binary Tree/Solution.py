# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum=0
        

        def height(root):
            if not root:
                return 0
            leftside=height(root.left)
            rightside=height(root.right)
            self.maximum=max(self.maximum,leftside+rightside)
            return max(leftside,rightside)+1
        height(root)
        return self.maximum
        
        
        