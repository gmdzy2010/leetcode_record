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


def main(head: ListNode):
    """重排链表

    穿针引线法，原地更新

    Args:
        - head (ListNode): 头节点
    """
    # * 用列表存储所有节点，后续可以用下标访问相应的位置
    nodes: List[ListNode] = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    # * 利用左右两个指针一一合并
    L, R = 0, len(nodes) - 1
    while L < R:
        # * 让 L 节点指向 R 处的节点
        nodes[L].next = nodes[R]
        L += 1

        # * 注意 L 先自增，所以有可能和 R 相等
        if L == R:
            break

        # * 让 R 处节点指向下一个 L 处节点
        nodes[R].next = nodes[L]
        R -= 1

    # * 由于 L 指针先走，最终也是先在 L 指针处停止，需要把此时 L 处节点的 next 置空
    nodes[L].next = None


if __name__ == "__main__":
    test_head = ListNode(1)
    test_head.next = ListNode(2)
    test_head.next.next = ListNode(3)
    test_head.next.next.next = ListNode(val=4, _next=ListNode(5))
    main(test_head)
    print(test_head)
