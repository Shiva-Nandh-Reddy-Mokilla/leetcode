# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0

            leftside=height(root.left)
            rightside=height(root.right)
            if leftside==-2:
                return -2
            if rightside==-2:
                return -2
            if abs(leftside-rightside)>1:
                return -2
            return max(leftside,rightside)+1
        return height(root)!=-2




        

        