"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #NLR
        
        ans =[]
        
        if root:
            ans.append(root.val)
            for child in root.children:
                ans.extend(self.preorder(child))
        return ans