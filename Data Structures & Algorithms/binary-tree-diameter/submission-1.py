# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_depth(self, root: Optional[TreeNode]): 
            if not root: 
                return 0
            return 1 + max(self.find_depth(root.left), self.find_depth(root.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        max_diameter = 0
        stack = [root]
        while stack: 
            node = stack.pop()
            current_diameter = self.find_depth(node.left) + self.find_depth(node.right)

            max_diameter = max(max_diameter, current_diameter)
            if node.left: 
                stack.append(node.left)
            if node.right: 
                stack.append(node.right)
        return max_diameter


        
        