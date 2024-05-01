from typing import Self, Set


class ListNode:
    """链表节点"""

    def __init__(self, val: int = 0, _next: Self | None = None):
        self.val = val
        self.next: Self | None = _next


def main(head: ListNode) -> ListNode | None:
    """判断链表有环无环

    Args:
        head (ListNode): 头节点

    Returns:
        ListNode | None: 环节点，无环则为空
    """
    visited: Set[ListNode] = set()
    curr = head

    while curr:
        if curr in visited:
            return curr
        visited.add(curr)
        curr = curr.next

    return None


if __name__ == "__main__":
    test_head = ListNode(1)
    cycle_node = test_head.next = ListNode(2)
    test_head.next.next = ListNode(3)
    test_head.next.next.next = ListNode(val=4, _next=cycle_node)
    ans = main(test_head)
    print(ans.val if ans else "无环")
