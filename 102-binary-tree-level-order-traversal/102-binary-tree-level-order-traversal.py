# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue , answer = deque([root]), []
        
        while queue:
            level = []
            
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            #level is traversed
            answer.append(level)
        #allthe levels are traversed
        return answer
    
#Note to myself : range(len(queue)) does not keep changing with every iteration. It is calculated only one time everytime we enter the while loop.

             
                