# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if root lies between p and q, they belong in different subtrees, hence root is the LCA
        
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        
        if p.val <= root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        return self.lowestCommonAncestor(root.right, p , q )

#time complexity - O(n) worst case we might visit all the nodes 
#space complexity - O(n) 