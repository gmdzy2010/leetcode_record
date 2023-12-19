from heapq import heappop, heappush
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

    def __lt__(self, other: Self) -> bool:
        return self.val < other.val


def main(lists: List[ListNode | None]) -> ListNode | None:
    """合并K个链表

    使用优先级队列
    - 优先级队列实际上是小根堆的数组表示，
    - 将所有头节点入堆后，每次出堆的即为值最小的节点
    - 需要注意入堆需要节点支持比较操作：
        - ACM模式：直接定义 dunder method -> __lt__(self, obj)
        - 核心代码模式：使用 monkeypatch 的方式将 __lt__ 绑定到 ListNode

    Args:
        lists (List[ListNode  |  None]): K个链表的头节点

    Returns:
        ListNode | None: 合并后的链表新节点
    """
    dummy = ListNode()
    curr = dummy

    # * 使用优先级队列维护K个列表的当前最小值（标准库使用小根堆）
    pq: List[ListNode] = []

    # * 构造优先级队列
    for node in lists:
        if node:
            heappush(pq, node)

    # *
    while pq:
        # * 从优先级队列出堆，出堆的节点即为K个头节点中值最小的节点
        min_node = heappop(pq)
        curr.next = ListNode(min_node.val)
        curr = curr.next

        # * 当前节点合并到总节点上后，当前节点的下一个节点继续入堆
        if min_node.next:
            heappush(pq, min_node.next)

    return dummy.next
