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


class MyLinkedList:
    """自定义链表"""

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """获取链表相应下标处的值

        Args:
            - index (int): 下标

        Returns:
            - int: 下标处的值
        """
        # * 处理越界
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            if curr:
                curr = curr.next

        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        """链表头部插入

        Args:
            - val (int): 待插入链表头部的值
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """链表尾部插入

        Args:
            - val (int): 待插入链表头部的值
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """在下标处插入节点

        Args:
            - index (int): 待插入位置（下标位置）
            - val (int): 待插入的节点值
        """
        if index > self.size:
            return

        index = max(0, index)

        curr = self.head
        for _ in range(index):
            if curr:
                curr = curr.next
            else:
                break

        if curr:
            _next = curr.next
            curr.next = ListNode(val)
            curr.next.next = _next
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """在下标处删除节点

        Args:
            - index (int): 待插入位置（下标位置）
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        for _ in range(index):
            if curr:
                curr = curr.next

        if curr and curr.next:
            _next = curr.next
            curr.next = curr.next.next
            _next.next = None
            self.size -= 1
