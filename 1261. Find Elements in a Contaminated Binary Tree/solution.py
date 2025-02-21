from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.recover(root, 0)

    def recover(self, node: Optional[TreeNode], value: int):
        if not node:
            return
        node.val = value
        self.values.add(value)
        self.recover(node.left, 2 * value + 1)
        self.recover(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return target in self.values
