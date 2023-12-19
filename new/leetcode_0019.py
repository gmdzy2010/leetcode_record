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


def main(head: ListNode, n: int) -> ListNode | None:
    """删除链表的倒数第N个节点

    使用快慢指针法
    - 让快指针从头节点出发先走N个节点
    - 让快指针和慢指针同时走，当快指针到达链表尾部时，慢指针正好到达倒数第N个节点
        - 注意为了好删除第N个节点，需要慢指针从 dummy 节点出发

    Args:
        - head (ListNode): 链表头节点
        - n (int): 要删除的节点位置

    Returns:
        ListNode | None: 删除节点后的链表头节点
    """
    dummy = ListNode(_next=head)
    fast_node = head
    slow_node = dummy

    for _ in range(n):
        if fast_node:
            fast_node = fast_node.next

    while fast_node and slow_node:
        fast_node = fast_node.next
        slow_node = slow_node.next

    if slow_node and slow_node.next:
        slow_node.next = slow_node.next.next

    return dummy.next


if __name__ == "__main__":
    test_head = ListNode(1)
    test_head.next = ListNode(2)
    test_head.next.next = ListNode(3)
    test_head.next.next.next = ListNode(val=4, _next=ListNode(5))
    main(test_head, 2)
