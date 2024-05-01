from typing import Self


class ListNode:
    """链表节点"""

    def __init__(self, val: int = 0, _next: Self | None = None):
        self.val = val
        self.next: Self | None = _next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


def main(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """两个链表相加

    Args:
        - l1 (ListNode | None): 链表1头节点
        - l2 (ListNode | None): 链表2头节点

    Returns:
        - ListNode | None: 链表相加后的新链表头节点
    """
    dummy = ListNode()
    curr = dummy

    total, carry = 0, 0
    while l1 or l2:
        if l1 and not l2:
            total = l1.val + carry
            l1 = l1.next
        elif l2 and not l1:
            total = l2.val + carry
            l2 = l2.next
        elif l1 and l2:
            total = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next

        carry, remainder = total // 10, total % 10
        curr.next = ListNode(remainder)
        curr = curr.next

    if carry != 0:
        curr.next = ListNode(carry)

    return dummy.next
