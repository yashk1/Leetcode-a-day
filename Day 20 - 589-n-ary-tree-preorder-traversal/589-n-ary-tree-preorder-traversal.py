"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        #there are values in tree
        stack ,answer = [root], []
        
        while stack: 
        #run untill we have traveresd all the elements in a tree. 
        #Since we are putting root firts andi then all it's children
        
            cur = stack.pop() #this is a pointer that stores the location of top value in stack
            answer.append(cur.val)
            
            stack.extend(reversed(cur.children)) #adding children from left to right
            
        return answer