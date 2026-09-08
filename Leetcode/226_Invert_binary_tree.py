class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root :
            return root
        t = root.left
        root.left = root.right
        root.right = t
        if root.left :
            self.invertTree(root.left)
        if root.right :
            self.invertTree(root.right)
        return root
        