def has_cycle_direct(head):
    all_node = []
    while head:
        if head in all_node:
            return True
        else:
            all_node.append(head)
            head = head.next
    return False


def has_cycle_double_pointer(head):
    slow = fast = head
    while slow and fast and fast.next:
        if fast.next == slow:
            return True
        else:
            slow = slow.next
            fast = fast.next.next
    return False
