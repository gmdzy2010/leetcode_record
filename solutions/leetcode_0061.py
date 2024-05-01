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


def main(head: ListNode | None, k: int) -> ListNode | None:
    """旋转链表

    - 遍历链表，计算链表长度
    - 当 k >= n 时，我们仅需要向右移动 k % n 次
    - 将尾节点指向头节点，构成一个环
    - 指针走到尾节点前一个节点位置，断开下一个节点和后面节点的联系
    - 此时节点即为旋转后链表的头节点

    Args:
        - head (ListNode | None): 头节点
        - k (int): 旋转位置，有可能比链表长度更大

    Returns:
        - ListNode | None: 旋转后的链表头节点
    """
    # * 如果链表为空或者长度小于2，链表不变
    if k == 0 or not head or not head.next:
        return head

    # * 统计链表长度，注意指针走到尾节点的前一个节点，所以长度从1开始计算
    size = 1
    curr = head
    while curr.next:
        size += 1
        curr = curr.next

    # * 当 k >= n 时，我们仅需要向右移动 k % n 次即可
    add = size - k % size

    # * 如果恰好旋转了链表长度的整数倍，那就是原链表
    if add == size:
        return head

    # * 将尾节点指向头节点，构成一个环
    curr.next = head

    # * 指针当前在原先尾节点的前一个节点位置，向前走 add 步
    while add and curr:
        curr = curr.next
        add -= 1

    # * 将指针处节点和后续的链表断开，指针节点的下一个节点即为旋转后链表的头节点
    new_head = curr.next  # type:ignore
    curr.next = None  # type:ignore

    return new_head
