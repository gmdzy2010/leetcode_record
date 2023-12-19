from typing import List, Self


class ListNode:
    """链表节点"""

    def __init__(self, val: int = 0, _next: Self | None = None):
        self.val = val
        self.next: Self | None = _next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


def main(head: ListNode, left: int, right: int) -> ListNode | None:
    """反转链表

    - 穿针引线法，常规方法
    - 头插法，时间和空间复杂度更优

    Args:
        - head (ListNode): 链表头节点
        - left (int): 左边界
        - right (int): 右边界

    Returns:
        - ListNode | None: 反转后的链表头节点
    """
    # reverse_part_common(head, left, right)
    reverse_part_head_insert(head, left, right)


def reverse_part_head_insert(
    head: ListNode,
    left: int,
    right: int,
) -> ListNode | None:
    """头插法

    Args:
        - head (ListNode): 链表头节点
        - left (int): 左边界
        - right (int): 右边界

    Returns:
        - ListNode | None: 反转后的链表头节点
    """
    if left == right:
        return head

    dummy = ListNode(-1, head)
    prev = dummy

    # * 先走到 left 节点的前一个位置
    for _ in range(left - 1):
        if not prev:
            break
        prev = prev.next

    if not prev:
        return head

    # * curr 指向待反转区域的第一个节点 left
    curr = prev.next
    for _ in range(right - left):
        if not curr:
            break

        # ... -> prev -> curr -> _next -> _next.next -> ...
        _next = curr.next

        if not _next:
            break

        after_next = _next.next

        # ! 穿针引线的三个步骤顺序不能变
        # * STEP 1. 先保持对当前节点下一个节点的引用
        # ... -> prev -> curr ----------> after_next -> ...
        #                        _next -> after_next -> ...
        curr.next = after_next

        # * STEP 2. 让 _next 的 next 指向 prev 的下一个节点
        # ... -> prev -> curr ----------> after_next -> ...
        #                curr <- _next
        # ? 这里为什么不能使用 curr 呢？
        # 因为这里的 prev.next 后面会有有变化，循环需要这种变化，而 curr 循环中不变
        _next.next = prev.next

        # * STEP 3. 让 prev 的 next 指向 _next
        # ... -> prev ---------> _next -> curr ----------> after_next -> ...
        prev.next = _next

    return dummy.next


def reverse_part_common(
    head: ListNode,
    left: int,
    right: int,
) -> ListNode | None:
    """穿针引线法

    Args:
        - head (ListNode): 链表头节点
        - left (int): 左边界
        - right (int): 右边界

    Returns:
        - ListNode | None: 反转后的链表头节点
    """
    if left == right:
        return head

    dummy = ListNode(-1, head)
    curr = dummy

    L = 0
    while curr:
        if L + 1 == left:
            r_tail = r_head = curr.next
            R = right
            while r_tail and R > L + 1:
                r_tail = r_tail.next
                R -= 1

            curr.next = reverse(r_head, r_tail)
            break

        curr = curr.next
        L += 1

    return dummy.next


def reverse(head: ListNode | None, tail: ListNode | None) -> ListNode | None:
    dummy = ListNode(-1, head)
    stack: List[ListNode] = []

    _next = tail.next if tail else None

    curr = head
    while curr and curr != _next:
        stack.append(curr)
        curr = curr.next

    curr = dummy
    while stack:
        node = stack.pop()
        node.next = None
        curr.next = node
        curr = curr.next

    curr.next = _next

    return dummy.next


if __name__ == "__main__":
    test_head = ListNode(1)
    test_head.next = ListNode(2)
    test_head.next.next = ListNode(3)
    test_head.next.next.next = ListNode(val=4, _next=ListNode(5))
    main(test_head, 2, 4)
