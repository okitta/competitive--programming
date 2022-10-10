# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        l=0
        while temp != None:
            l+=1
            temp = temp.next
        if l==1:
            return head
        temp = head
        n=0
        while temp != None:
            if n == l//2:
                return temp
            temp = temp.next
            n+=1
