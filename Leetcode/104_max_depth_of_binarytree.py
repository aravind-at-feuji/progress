class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(node) :
            if not node :
                return 0
            return 1 + max(depth(node.left),depth(node.right))
        return depth(root)
