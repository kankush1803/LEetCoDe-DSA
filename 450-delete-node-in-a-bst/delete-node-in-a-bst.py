# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Step 1: Search for the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Step 2: Node found – handle deletion
            
            # Case 1 & 2: Node has 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 3: Node has 2 children
            # Find the in-order successor (minimum node in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Replace root's value with the in-order successor's value
            root.val = curr.val
            
            # Delete the in-order successor
            root.right = self.deleteNode(root.right, curr.val)
            
        return root