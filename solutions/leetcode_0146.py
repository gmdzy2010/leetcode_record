from typing import Dict, Self


class ListNode:
    """一个双向链表"""

    def __init__(self, key: int, value: int = -1):
        self.key = key
        self.value = value
        self.prev: Self | None = None
        self.next: Self | None = None


class LRUCache:
    """最近最少使用缓存(Least Recently Used)算法的简单实现"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap: Dict[int, ListNode] = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)

        # * 初始化缓存对象实例时，设置 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_node_on_tail(self, node: ListNode):
        """将节点插入到尾节点和尾节点前一个节点之间

        Args:
            node (ListNode): 待插入节点
        """
        # 再改待插入节点的前后关联
        # ..............    node -> self.tail
        # self.tail.prev <- node    .........
        node.next = self.tail
        node.prev = self.tail.prev

        # 改尾节点的前一个节点的后关联
        # self.tail.prev -> node    .........
        if self.tail.prev:
            self.tail.prev.next = node

        # 改尾节点的前关联
        # ..............    node <- self.tail
        self.tail.prev = node

    def _move_node_to_tail(self, key: int):
        target_node = self.hashmap.get(key)
        if target_node and target_node.prev and target_node.next:
            # * 从链表中将目标节点摘除
            # target_node.prev <-> target_node.next
            target_node.next.prev = target_node.prev
            target_node.prev.next = target_node.next

            self._insert_node_on_tail(target_node)

    def get(self, key: int) -> int:
        """缓存获取
        - 平均时间复杂度：O(1)

        规则
        - 如果关键字 key 存在于缓存中，则返回关键字的值，
        - 否则返回 -1

        Args:
            key (int): 缓存的键

        Returns:
            int: 缓存的值
        """
        if key in self.hashmap:
            self._move_node_to_tail(key)

        node = self.hashmap.get(key)

        return node.value if node else -1

    def put(self, key: int, value: int):
        """缓存更新

        - 如果关键字 key 已经存在，则变更其数据值 value ；
        - 如果不存在，则向缓存中插入该组 key-value 。
        - 如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字

        Args:
            key (int): 缓存的键
            value (int): 缓存的值
        """
        if key in self.hashmap:
            self.hashmap[key].value = value
            self._move_node_to_tail(key)
            return None

        if len(self.hashmap) == self.capacity:
            most_cold_node = self.head.next
            if most_cold_node:
                self.hashmap.pop(most_cold_node.key)

            if self.head.next:
                self.head.next = self.head.next.next

            if self.head.next:
                self.head.next.prev = self.head

        new_node = ListNode(key, value)
        self.hashmap[key] = new_node
        self._insert_node_on_tail(new_node)

        return None


if __name__ == "__main__":
    obj = LRUCache(2)
    obj.put(1, 22)
    obj.put(2, 44)
    print(obj.get(1))
    obj.put(3, 6)
    print(obj.get(2))
    obj.put(4, 8)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))
