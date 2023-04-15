# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # completed on 4/7/2023

        orig = head
        parse = head

        try:
            while head.next != None:
                # if current parse val is greater than current head val, that is the next node to add to SLL
                if parse.val > head.val:
                    head.next = parse
                    head = head.next
                # if parse next is None, then end of SLL has been reached and last element was duplicate of previous
                elif parse.next == None:
                    head.next = None
                    break
                # look at next element
                parse = parse.next
            return orig
        except:
            return orig
