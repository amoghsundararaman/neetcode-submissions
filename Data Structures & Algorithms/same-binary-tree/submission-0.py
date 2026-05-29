class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if root1 is None and root2 is None: 
                return True
            elif root1 is None or root2 is None: 
                return False
            elif root1.val == root2.val: 
                left = dfs(root1.left, root2.left)
                right = dfs(root1.right, root2.right)

                if left and right: 
                    return True
                else: 
                    return False
            else: 
                return False
        return dfs(p, q)