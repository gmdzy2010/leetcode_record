def detect_cycle_start_double_pointer(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            index_1, index_2 = fast, head
            while index_1 != index_2:
                index_1 = index_1.next
                index_2 = index_2.next
            return index_2


def detect_cycle_start_hash(head):
    current, node_set = head, set()
    while current:
        if current in node_set:
            return current
        else:
            node_set.add(current)
            current = current.next
