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
    """删除链表中的重复节点

    Args:
        head (ListNode | None): 头节点

    Returns:
        ListNode | None: 删除重复节点后的头节点
    """
    if not head or not head.next:
        return head

    dummy = ListNode(-1, head)
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next


if __name__ == "__main__":
    test_head = ListNode(1)
    test_head.next = ListNode(1)
    test_head.next.next = ListNode(2)
    test_head.next.next.next = ListNode(val=2, _next=ListNode(3))
    main(test_head)
