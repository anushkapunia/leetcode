# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        
        if head == None or head.next == None:
            return True

        s = head 
        f = head
        while f != None and f.next != None:
            s = s.next
            f = f.next.next
            
        p = None
        while s != None:
            n = s.next
            s.next = p
            p = s
            s = n
            
        l , r = head , p
        while r !=None:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
            
        return True
            
        
        