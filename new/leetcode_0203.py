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


def main(head: ListNode | None, val: int) -> ListNode | None:
    """移除链表节点

    Args:
        - head (ListNode | None): 原链表头节点
        - val (int): 待移除的节点值

    Returns:
        - ListNode | None: 移除节点后的链表头节点
    """
    dummy = ListNode()
    dummy.next = head
    prev = dummy

    while prev.next:
        if prev.next.val == val:
            curr = prev.next
            prev.next = prev.next.next
            curr.next = None
        else:
            prev = prev.next

    return dummy.next


if __name__ == "__main__":
    test_head = ListNode(val=1)
    test_head.next = ListNode(val=1)
    test_head.next.next = ListNode(val=1)
    test_head.next.next.next = ListNode(val=1)
    test_head.next.next.next.next = ListNode(val=1)
    test_head.next.next.next.next.next = ListNode(val=1)
    print(main(test_head, 1))
