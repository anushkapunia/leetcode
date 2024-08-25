# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        if head.next is None :
            return head.next
        
        d = ListNode(0)
        d.next = head
        
        f = d
        s = d
        
        for i in range(n):
            f = f.next
            
        while f.next:
            f = f.next
            s = s.next
            
        s.next = s.next.next
            
        return d.next

            
        
            
        