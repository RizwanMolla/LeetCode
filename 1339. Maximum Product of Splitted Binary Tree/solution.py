class Solution:
    MOD = 10**9 + 7

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)

        self.best = 0

        def subtree_sum(node):
            if not node:
                return 0
            s = node.val + subtree_sum(node.left) + subtree_sum(node.right)
            self.best = max(self.best, s * (total - s))
            return s

        subtree_sum(root)
        return self.best % self.MOD
