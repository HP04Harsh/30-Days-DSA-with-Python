class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  dummy = ListNode(0, head)
  fast = slow = dummy

  # Fast pointer ko n steps aage badhao
  for _ in range(n):
    fast = fast.next

  # Dono pointers ko saath me aage badhao
  while fast.next:
    fast = fast.next
    slow = slow.next

  # Target node skip kar do
  slow.next = slow.next.next
  return dummy.next