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


def main(head: ListNode | None, x: int) -> ListNode | None:
    """分隔链表

    Args:
        head (ListNode | None): 原链表头节点
        x (int): 分隔阈值

    Returns:
        ListNode | None: 分隔后的新链表头节点
    """
    dummy_S = ListNode()
    dummy_L = ListNode()
    curr, S, L = head, dummy_S, dummy_L

    while curr:
        if curr.val < x:
            S.next = curr
            S = S.next
        else:
            L.next = curr
            L = L.next

        curr = curr.next

    # ! 这里 L.next 不置空提交至 leetcode 会超内存限制
    # ? 确实可以立即减少内存，但是leetcode 的内存监测会这么精准？监测到对象多创建了一个？
    L.next = None
    S.next = dummy_L.next

    return dummy_S.next


if __name__ == "__main__":
    test_head = ListNode(1)
    test_head.next = ListNode(1)
    test_head.next.next = ListNode(2)
    test_head.next.next.next = ListNode(val=2, _next=ListNode(3))
    main(test_head, 3)
