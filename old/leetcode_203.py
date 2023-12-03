class ListNode:
    
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node


def remove_specified_node(head, value):
    temp_node = current = ListNode()
    temp_node.next_node = head
    while current.next_node:
        if current.next_node.value == value:
            current.next_node = current.next_node.next_node
        else:
            current = current.next_node
    return temp_node.next_node
