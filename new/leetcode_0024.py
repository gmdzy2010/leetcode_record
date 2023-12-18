from typing import Self, Tuple


class ListNode:
    """链表节点"""

    def __init__(self, val: int = 0, _next: Self | None = None):
        self.val = val
        self.next: Self | None = _next

    def __str__(self) -> str:
        return f"node -> {self.val}"

    def __repr__(self) -> str:
        return f"node -> {self.val}"


def main(head: ListNode | None) -> ListNode | None:
    """两两交换链表中的节点

    Args:
        head (ListNode | None): 头节点

    Returns:
        ListNode | None: 交换操作之后的节点
    """
    if not head:
        return head

    dummy = ListNode(val=-1, _next=head)
    curr = dummy
    first_node = head
    second_node = head.next

    while curr and first_node and second_node:
        _next = second_node.next
        first_node, second_node = swap(first_node, second_node)
        curr.next = first_node

        first_node = _next
        if _next:
            second_node = _next.next

        curr = curr.next.next

    return dummy.next


def swap(node1: ListNode, node2: ListNode) -> Tuple[ListNode, ListNode]:
    """交换两个相邻节点

    Args:
        node1 (ListNode): 节点1
        node2 (ListNode): 节点2

    Returns:
        Tuple[ListNode, ListNode]: 交换后的节点
    """
    _next = node2.next
    node2.next = node1
    node1.next = _next

    return node2, node1
