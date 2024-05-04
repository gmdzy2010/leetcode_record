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
    """归并排序链表
    - 自顶向下，时间复杂度：O(nlogn)，空间复杂度：O(logn)
    - 自底向上，时间复杂度：O(nlogn)，空间复杂度：O(1)

    Args:
        - head (ListNode | None): 头节点

    Returns:
        - ListNode | None: 排好序的链表头节点
    """
    head = merge_sort_via_top_down(head)
    # merge_sort_via_bottom_up(head)

    return head


def merge_sort_via_top_down(head: ListNode | None) -> ListNode | None:
    """排序链表
    - 使用归并排序

    Args:
        head (ListNode | None): 头节点

    Returns:
        ListNode | None: 排好序的链表头节点
    """
    if not head:
        return head

    return sort_top_down(head, None)


def sort_top_down(
    head: ListNode | None,
    tail: ListNode | None,
) -> ListNode | None:
    """自顶向下归并排序函数

    Args:
        head (ListNode): 头节点
        tail (ListNode): 尾节点

    Returns:
        ListNode: 排序后头节点
    """
    if not head:
        return head

    # ! 如果头节点和尾节点相邻，需要截断他们之间的联系
    # ? 为什么
    # * 因为最终归并的时候不切断，会导致多余的部分合并到最终链表中
    if head.next == tail:
        head.next = None
        return head

    # * 使用快慢指针找到中间的节点
    S = F = head
    while S and F and F != tail:
        S = S.next
        F = F.next
        if F and F != tail:
            F = F.next

    # * 此时慢指针即为中点处节点
    M = S

    return merge(sort_top_down(head, M), sort_top_down(M, tail))


def merge(head1: ListNode | None, head2: ListNode | None) -> ListNode | None:
    """合并函数
    - 按照节点值大小依次合并至一个链表

    Args:
        head1 (ListNode): 链表1头节点
        head2 (ListNode): 链表2头节点

    Returns:
        ListNode | None: 合并后的头节点
    """
    dummy = ListNode(-1)
    curr, curr1, curr2 = dummy, head1, head2
    while curr1 and curr2:
        if curr1.val <= curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next

    if curr1:
        curr.next = curr1
    if curr2:
        curr.next = curr2

    return dummy.next


def merge_sort_via_bottom_up(head: ListNode | None) -> ListNode | None:
    """排序链表
    - 使用归并排序

    Args:
        head (ListNode | None): 头节点

    Returns:
        ListNode | None: 排好序的链表头节点
    """
    if not head:
        return head

    dummy = ListNode(val=-1, _next=head)

    # * 先求得链表的总长度
    size = 0
    curr = head
    while curr:
        size += 1
        curr = curr.next

    sub_size = 1
    while sub_size < size:
        prev, curr = dummy, dummy.next
        while curr:
            head1 = curr
            for _ in range(1, sub_size):
                if curr.next:
                    curr = curr.next
                else:
                    break
            # * 切断后续节点之前先保留对后续的节点的引用
            head2 = curr.next

            # * 切断后续的节点
            curr.next = None

            # * 开始后半部分的排序
            curr = head2
            for _ in range(1, sub_size):
                if curr and curr.next:
                    curr = curr.next
                else:
                    break

            # ? 对后继部分的处理？
            succ = None
            if curr:
                succ = curr.next
                curr.next = None

            # * 合并两个链表
            merged = merge(head1, head2)
            prev.next = merged
            while prev.next:
                prev = prev.next

            # *
            curr = succ

        # *
        sub_size <<= 1

    return dummy.next


if __name__ == "__main__":
    test_head = ListNode(2)
    test_head.next = ListNode(1)
    test_head.next.next = ListNode(4)
    test_head.next.next.next = ListNode(6)
    test_head.next.next.next.next = ListNode(5, _next=ListNode(3))
    print(main(test_head))
