# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        
        sp = head
        fp = head.next
        
        while sp != fp:
            if fp is None or fp.next is None:
                return False
            sp = sp.next
            fp = fp.next.next
            
            
        return True