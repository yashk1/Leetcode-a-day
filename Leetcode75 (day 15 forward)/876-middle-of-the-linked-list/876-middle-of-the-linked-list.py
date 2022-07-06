# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #put everything in array and return the middle element
        arr = []
        
        while head: #loop until the head points to null. last node will point to null
            arr.append(head)
            head = head.next
        return arr[len(arr)//2]
    
    
    
    
        
        