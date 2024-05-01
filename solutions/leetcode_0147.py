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
    """排序链表
    - 使用插入排序

    Args:
        head (ListNode | None): 头节点

    Returns:
        ListNode | None: 排好序的链表头节点
    """
    if not head:
        return head

    dummy = ListNode(val=-1, _next=head)

    # * 记录已排好序的最后一个节点
    last_sorted = head

    # * 待插入节点，从头节点的下一个节点开始
    curr = head.next
    while last_sorted and curr:
        # * 跳过已经排好序的部分
        if last_sorted.val <= curr.val:
            last_sorted = last_sorted.next
        else:
            # * 涉及修改 next 指向的操作，需要从 dummy 开始而不是 head
            prev = dummy

            # * 在已经排序的部分找到第一个比待插入节点值大的节点：prev 的下一个节点
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            # * 将待插入节点插到 prev 之后，也就是 last_sorted 之前，原始位置关系如下：
            # ... -> prev -> last_sorted -> curr -> curr.next -> ...

            # * STEP 1. 修改 last_sorted 的 next 指向
            # ... -> prev -> last_sorted ---------> curr.next -> ...
            #                               curr -> curr.next -> ...
            last_sorted.next = curr.next

            # * STEP 2. 修改 curr 的 next 指向
            # ... -> prev -> last_sorted ---------> curr.next -> ...
            # ... -> prev -> last_sorted <- curr
            curr.next = prev.next

            # * STEP 3. 修改 curr 的 next 指向
            # ... -> prev -> last_sorted ---------> curr.next -> ...
            # ... -> prev -> last_sorted <- curr
            # ... -> prev ----------------> curr
            prev.next = curr

            # 拉平后的链表即为
            # ... -> prev -> curr -> last_sorted -> curr.next -> ...

        if not last_sorted:
            break

        # * 将待比较是否要插入的节点指向 已排序最后一个节点的下一个节点
        curr = last_sorted.next

    return dummy.next


if __name__ == "__main__":
    test_head = ListNode(2)
    test_head.next = ListNode(1)
    test_head.next.next = ListNode(4)
    test_head.next.next.next = ListNode(6)
    test_head.next.next.next.next = ListNode(5, _next=ListNode(3))
    print(main(test_head))
