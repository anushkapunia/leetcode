# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        s = []
        temp = head
        
        while temp != None:
            s.append(temp.val)
            temp = temp.next
           
        temp = head
        for i in range(len(s)//2):
            sv = s.pop()
            if sv == temp.val:
                temp = temp.next
            else:
                return False
            
        return True

            
        