​# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        level=0
        q = deque([root,])
        
        while q:
            
            levels.append([])
            
            level_length = len(q)
            
            for i in range(level_length):
                node= q.popleft()
                
                levels[level].append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level +=1
        return levels


--------------------------------
OR

Breadh First Search

Using BFS, at any instant only L1 and L1+1 nodes are in the queue.
When we start the while loop, we have L1 nodes in the queue.
for _ in range(len(q)) allows us to dequeue L1 nodes one by one and add L2 children one by one.
Time complexity: O(N). Space Complexity: O(N)

q, result = deque(), []
        if root:
            q.append(root)
        while len(q):
            level = []
            for _ in range(len(q)):
                x = q.popleft()
                level.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            result.append(level)
        return result



------------------
OR


class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, result = deque([root]), []
        
        while queue:
            level = [] #hold the values at curretn level
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level)
        return result


Note to myself : range(len(queue)) does not keep changing with every iteration. It is calculated only one time everytime we enter the while loop.

------------------

q, result = deque(),[]
        
        if root:
            q.append(root)
        while len(q):
            level=[]
            for i in range(len(q)):
                x = q.popleft()
                level.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                
            result.append(level)
            
        return result