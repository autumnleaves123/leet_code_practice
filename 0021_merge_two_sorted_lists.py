# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # completed on 3/26/2023 (took a couple days)

        # head starts with the smallest value from list1 or list2 node
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val <= list2.val:
            head = list1
            list1 = list1.next #iterate list1
        else: #list2.val <= list1.val
            head = list2
            list2 = list2.next #iterate list2

        itr = head

        while list1 != None or list2 != None:
            # no more elements in list1
            if list1 == None:
                itr.next = list2
                break
            # no more elements in list2
            elif list2 == None:
                itr.next = list1
                break
            elif list1.val <= list2.val:
                itr.next = list1
                itr = itr.next # iterate itr
                list1 = list1.next # iterate list1
            else: # list2.val <= list1.val
                itr.next = list2
                itr = itr.next # iterate itr
                list2 = list2.next # iterate list2

        return head
