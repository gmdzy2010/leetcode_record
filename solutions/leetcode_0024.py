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


def main(head: ListNode | None) -> ListNode | None:
    """两两交换链表节点

    Args:
        - head (ListNode | None): 头节点

    Returns:
        - ListNode | None: 两两交换之后的头节点
    """
    dummy = ListNode()
    dummy.next = head
    curr = dummy

    while curr and curr.next and curr.next.next:
        node1 = curr.next
        node2 = curr.next.next

        curr.next = node2
        node1.next = node2.next
        node2.next = node1

        # * 此时的node1为未交换节点的前一个节点
        curr = node1

    return dummy.next
