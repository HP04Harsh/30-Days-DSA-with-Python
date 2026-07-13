# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0: return head
        vals, curr = [], head
        while curr: vals.append(curr.val); curr = curr.next
        k, curr = k % len(vals), head
        vals = vals[-k:] + vals[:-k]
        while curr: curr.val = vals.pop(0); curr = curr.next
        return head