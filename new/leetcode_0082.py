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
    """删除排序链表中的重复节点

    Args:
        head (ListNode | None): 头节点

    Returns:
        ListNode | None: 删除重复节点后的头节点
    """
    if not head or not head.next:
        return head

    dummy = ListNode(-1, head)

    # ! 由于头节点有可能重复而被删除，遍历需要从 dummy 节点开始
    curr = dummy

    while curr.next and curr.next.next:
        # * 先找到第一个节点值重复的节点
        if curr.next.val == curr.next.next.val:
            duplicate_val = curr.next.val

            # * 对所有重复的节点进行删除
            while curr.next and curr.next.val == duplicate_val:
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
