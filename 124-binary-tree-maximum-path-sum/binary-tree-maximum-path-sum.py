# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0
            
            # Max contribution from left and right children (ignore negative sums)
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            
            # Current node as the root/highest point of the path
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)
            
            # Return max gain the parent node can get from this subtree
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum