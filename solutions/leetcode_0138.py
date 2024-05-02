from typing import Dict, Self


class ListNode:
    """链表节点"""

    def __init__(
        self,
        val: int = 0,
        _next: Self | None = None,
        random: Self | None = None,
    ):
        self.val = val
        self.next: Self | None = _next
        self.random: Self | None = random

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


def copyRandomList(head: ListNode | None) -> ListNode | None:
    if not head:
        return

    visited: Dict[ListNode, ListNode] = {}

    curr = head
    while curr:
        visited[curr] = ListNode(curr.val)
        curr = curr.next

    curr = head
    while curr:
        visited[curr].next = visited.get(curr.next)  # type: ignore
        visited[curr].random = visited.get(curr.random)  # type: ignore
        curr = curr.next

    return visited[head]
