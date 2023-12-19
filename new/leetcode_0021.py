from typing import Self


class ListNode:
    """单链表节点"""

    def __init__(self, val: int = 0, _next: Self | None = None):
        self.val: int = val
        self.next: Self | None = _next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


def main(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """合并两个有序链表

    Args:
        list1 (ListNode | None): 第一个链表的头节点
        list2 (ListNode | None): 第二个链表的头节点

    Returns:
        ListNode | None: 合并后的链表头节点
    """
    dummy = ListNode()

    curr = dummy

    # * 根据值大小拼接链表
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    # * 将两个链表没有合并完的部分直接接上去
    curr.next = list1 if list1 else list2

    return dummy.next


if __name__ == "__main__":
    arr_1 = [2, 5, 8, 9]
    head_node_1 = ListNode(1)

    curr_node = head_node_1
    for i, e in enumerate(arr_1):
        curr_node.next = ListNode(e)
        curr_node = curr_node.next

    arr_2 = [4, 6, 7]
    head_node_2 = ListNode(3)

    curr_node = head_node_2
    for i, e in enumerate(arr_1):
        curr_node.next = ListNode(e)
        curr_node = curr_node.next

    node = main(head_node_1, head_node_2)
    print(node)
