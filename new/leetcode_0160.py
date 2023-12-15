from typing import Self


class ListNode:
    """一个双向链表"""

    def __init__(self, key: int, value: int = -1):
        self.key = key
        self.value = value
        self.prev: Self | None = None
        self.next: Self | None = None


def main(headA: ListNode, headB: ListNode) -> ListNode | None:
    """相交链表

    与二叉树最近公共祖先类似的处理办法，
    - 使用集合记录其中一个链表所有的节点，
    - 遍历第二个链表直到在集合中找到相交的节点即可

    Args:
        headA (ListNode): 链表A头节点
        headB (ListNode): 链表B头节点

    Returns:
        ListNode | None: 相交的节点或者空
    """
    a_visited = set()
    curr = headA
    while curr:
        a_visited.add(curr)
        curr = curr.next

    curr = headB
    while curr and curr not in a_visited:
        curr = curr.next

    return curr


if __name__ == "__main__":
    test_head_A = ListNode(9)
    test_head_A.next = ListNode(1)
    test_head_A.next.next = ListNode(2)
    test_head_A.next.next.next = ListNode(4)

    test_head_B = ListNode(3)
    test_head_B.next = ListNode(2)
    test_head_B.next.next = ListNode(4)

    print(main(test_head_A, test_head_B))
