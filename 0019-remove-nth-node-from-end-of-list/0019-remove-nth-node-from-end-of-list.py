# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp = head
        c = 0
        while temp is not None:
            c+=1
            temp = temp.next
            
        s = c-n 
        t = head
        p = None
        while s:
            p = t
            t = t.next
            s-=1
            
        if p is not None:
            p.next = t.next  # Bypass the node `t`
        else:
            head = t.next  # Special case: if the head itself is to be removed
        
        return head
        
     
            
        
            
