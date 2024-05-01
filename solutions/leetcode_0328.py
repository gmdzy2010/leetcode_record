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
    """奇偶链表

    Args:
        head (ListNode | None): 头节点

    Returns:
        ListNode | None: 排好序的链表头节点
    """
    if not head:
        return head

    O_head, E_head = head, head.next
    # * 奇数节点从头节点开始，偶数节点从头节点的下一个节点开始
    O, E = head, E_head

    # ! 从偶数节点开始遍历
    while E and E.next:
        # * 奇数节点的 next 指向偶数节点的下一个节点（奇数节点）
        O.next = E.next

        # * 奇数节点向前一步
        O = O.next

        # * 由于奇数节点已经向前了一步（来到了下一个奇数节点），其下一个节点为偶数节点
        E.next = O.next

        # * 偶数节点向前一步
        E = E.next

    # * 将奇数尾节点和偶数头节点连接起来即可
    O.next = E_head

    return O_head


if __name__ == "__main__":
    test_head = ListNode(1)
    test_head.next = ListNode(2)
    test_head.next.next = ListNode(3)
    test_head.next.next.next = ListNode(4)
    test_head.next.next.next.next = ListNode(5)
    print(main(test_head))
