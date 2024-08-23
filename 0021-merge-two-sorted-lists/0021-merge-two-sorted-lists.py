# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        d = ListNode(-1)
        temp = d
        
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
                
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
          
        while list1 != None :
            temp.next = list1
            temp = list1
            list1 = list1.next
            
        while list2!= None:
            temp.next = list2
            temp = list2
            list2 = list2.next
            
        return d.next
                
                
        