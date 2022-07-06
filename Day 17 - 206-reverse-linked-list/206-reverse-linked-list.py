# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head
        
        while curr:
            
            temp = curr.next #storing 2nd node in temp
            curr.next = prev #breaking the relation from node 1 to node 2 and pointing to null
            prev = curr
            curr = temp
            
        return prev #not sure about this