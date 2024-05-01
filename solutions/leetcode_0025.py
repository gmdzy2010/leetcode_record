from typing import Self, Tuple


class ListNode:
    """链表节点"""

    def __init__(self, val: int = 0, _next: Self | None = None):
        self.val = val
        self.next: Self | None = _next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


def reverse(head: ListNode, tail: ListNode) -> Tuple[ListNode, ListNode]:
    """反转一个子链表

    假设链表的头节点之前还存在一个虚拟节点 prev，在子链表反转的时候，
    - 使用 prev 保持对尾节点下一个节点的引用（这样可以保证尾节点之后的链表不被丢失），
    - 使用 curr 保持对头节点的引用
    - 此时可对链表每个节点实施反转：
        - _next -> 当前节点的下一个节点
        - 将当前节点的 next 属性指向 prev
            - ... prev    curr -> _next ...
            - ... prev <- curr    _next ...
        - curr 作为下一轮的 prev
        - _next 作为下一轮的 curr
        - 重复上述过程，直到到达尾节点终止循环

    Args:
        head (ListNode): 子链表的头节点
        tail (ListNode): 子链表的尾节点

    Returns:
        Tuple[ListNode, ListNode]: 反转后的链表头节点和尾节点
    """
    # * prev 引用尾节点的下一个节点
    prev = tail.next
    curr = head

    # * 反转子链表的每个节点
    while curr and prev != tail:
        _next = curr.next
        curr.next = prev

        prev = curr
        curr = _next

    return tail, head


def reverse_in_group(head: ListNode | None, k: int) -> ListNode | None:
    """K个一组反转链表

    Args:
        head (ListNode): 头节点
        k (int): 每组的节点个数

    Returns:
        ListNode: 反转后的链表头节点
    """
    # * 准备好 dummy 节点
    dummy = ListNode()
    dummy.next = head
    prev = dummy

    # * 从头节点处开始循环，每k个进行反转
    while head:
        # * 子链表的尾节点指针 tail 从 prev 开始
        tail = prev

        # * 让尾节点指针走到子链表尾节点处，如果子链表长度比k小，直接返回即可
        for _ in range(k):
            tail = tail.next
            if tail is None:
                return dummy.next

        # * 反转子链表会导致子链表尾节点之后的节点丢失，用 _next 保持对他们的引用
        _next = tail.next

        # * 反转链表
        head, tail = reverse(head, tail)

        # * 把子链表重新接回新链表
        prev.next = head
        tail.next = _next

        # * 下一轮循环准备
        prev = tail
        head = tail.next

    return dummy.next


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 6, 7, 8, 9]
    head_node = ListNode(1)

    curr_node = head_node
    for i, e in enumerate(arr):
        curr_node.next = ListNode(e)
        curr_node = curr_node.next

    reverse_in_group(head_node, 3)
