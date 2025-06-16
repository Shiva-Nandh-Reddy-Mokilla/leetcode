# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetry(one:TreeNode,two:TreeNode)->bool:
            if not one and not two:
                return True
            if not one or not two:
                return False
            if one.val!=two.val:
                return False
            return symmetry(one.left,two.right) and symmetry(one.right,two.left)
        if not root: return True
        return symmetry(root.left,root.right)
        

            
             

        
        