from typing import List, Self


class ListNode:
    """链表节点"""

    def __init__(self, val: int = 0, _next: Self | None = None):
        self.val = val
        self.next: Self | None = _next

    def __str__(self) -> str:
        return f"node -> {self.val}"

    def __repr__(self) -> str:
        return f"node -> {self.val}"


def reverse_1(head: ListNode) -> ListNode:
    """反转单链表

    使用额外的O(N)空间

    Args:
        head (ListNode): 头节点

    Returns:
        ListNode: 反转后的头节点
    """
    curr = head.next
    nodes: List[ListNode] = []
    while curr:
        nodes.append(curr)
        curr = curr.next

    curr = head
    for node in reversed(nodes):
        curr.next = node
        curr = curr.next

    return head


def reverse_2(head: ListNode) -> ListNode | None:
    """反转单链表

    循环版本

    Args:
        head (ListNode): 头节点

    Returns:
        ListNode | None: 反转后链表的头节点
    """
    prev = None
    curr = head
    while curr:
        _next = curr.next
        curr.next = prev

        prev = curr
        curr = _next

    return prev


def reverse_3(
    current: ListNode | None, previous: ListNode | None = None
) -> ListNode | None:
    """反转单链表

    递归版本

    Args:
        current (ListNode | None): 当前节点
        previous (ListNode | None): 前一个节点

    Returns:
        ListNode | None: 反转后链表的头节点
    """
    if current is None:
        return previous

    new_current = current.next
    current.next = previous

    return reverse_3(new_current, previous=current)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head_node = ListNode()

    curr_node = head_node
    for i, e in enumerate(arr):
        new_node = ListNode(e)
        curr_node.next = new_node
        curr_node = curr_node.next

    reverse_2(head_node)
