class ListNode:
    
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node


def reverse_linked_list_direct(head):
    node_value_list = []
    while head:
        node_value_list.append(head.value)
        head = head.next_node
    new_head = current = ListNode()
    for value in node_value_list[::-1]:
        current.next_node = ListNode(value)
        current = current.next_node
    return new_head.next_node


def reverse_linked_list_double_pointer(head):
    current, previous = head, None
    while current:
        # Store the left linked-list with temp in order to avoid losing it.
        new_head = current.next_node
        
        # Reverse the direction from next to previous.
        current.next_node = previous
        
        # Mark current node as the next "previous" node
        previous = current
        
        # Use node stored on step 1 as the new head node as the current node.
        current = new_head
    return previous


def reverse(current, previous):
    if current is None:
        return previous
    new_head = current.next_node
    current.next_node = previous
    return reverse(new_head, current)


def reverse_linked_list_recursion(head):
    return reverse(head, None)


if __name__ == '__main__':
    # Create a linked-list.
    test_head = test_current = ListNode()
    for n in range(1, 6):
        test_current.next_node = ListNode(n)
        test_current = test_current.next_node
    
    # test_new_head = reverse_linked_list_direct(test_head.next)
    # test_new_head = reverse_linked_list_double_pointer(test_head.next_node)
    test_new_head = reverse_linked_list_recursion(test_head.next_node)
    while test_new_head:
        print(test_new_head.value)
        test_new_head = test_new_head.next_node
