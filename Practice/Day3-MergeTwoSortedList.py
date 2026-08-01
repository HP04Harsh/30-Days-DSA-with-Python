class ListNode:

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
  dummy = cur = ListNode(0)

  while l1 and l2:
    if l1.val < l2.val:
      cur.next, l1 = l1, l1.next
    else:
      cur.next, l2 = l2, l2.next
    cur = cur.next

  cur.next = l1 or l2  # Jo bacha ho use attach kar do
  return dummy.next