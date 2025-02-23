from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_index = {val: i for i, val in enumerate(postorder)}
        
        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root
            
            left_root_val = preorder[pre_start + 1]
            left_post_idx = post_index[left_root_val]
            left_size = left_post_idx - post_start + 1

            root.left = build(pre_start + 1, pre_start + left_size, post_start, left_post_idx)
            root.right = build(pre_start + left_size + 1, pre_end, left_post_idx + 1, post_end - 1)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
