# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        try:
            sp = head
            fp = head.next
            
            while sp != fp:
                sp = sp.next
                fp = fp.next.next
                
            return True
        except:
            return False