# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # find middle of linkedlist
        # reverse second half of linkedlist 
        second = slow.next
        slow.next = None
        prev = None 
        while second: 
            dmy = second.next 
            second.next = prev
            prev = second 
            second = dmy 
        #merge two together
        list1,list2 = head,prev 
        while list2: 
            dmy1 = list1.next
            dmy2 = list2.next 
            list1.next = list2
            list2.next = dmy1 
            list1, list2 = dmy1,dmy2
        




    
      # reverse second half
      # merge two lists together
