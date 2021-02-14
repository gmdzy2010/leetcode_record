class ListNode:
    
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node


class SingleLinkedList:
    """A simple implementation of SingleLinkedList."""
    
    def __init__(self):
        """Initialize your data structure here."""
        self._virtual_head = ListNode()
        self._size = 0
    
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index
        is invalid, return -1.
        """
        if index < 0 or index > self._size - 1:
            return -1
        current = self._virtual_head.next_node
        while index:
            current = current.next_node
            index -= 1
        return current.value
    
    def add_at_head(self, value):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the
        linked list.
        """
        new_node = ListNode(value)
        new_node.next_node = self._virtual_head.next_node
        self._virtual_head.next_node = new_node
        self._size += 1
    
    def add_at_tail(self, value):
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(value)
        current = self._virtual_head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
        self._size += 1
    
    def add_at_index(self, index, value):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than the
        length, the node will not be inserted.
        """
        if index > self._size:
            return None
        new_node = ListNode(value)
        current = self._virtual_head
        while index:
            current = current.next_node
            index -= 1
        new_node.next_node = current.next_node
        current.next_node = new_node
        self._size += 1
    
    def delete_at_index(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self._size - 1 or index < 0:
            return None
        current = self._virtual_head
        while index:
            current = current.next_node
            index -= 1
        current.next_node = current.next_node.next_node
        self._size -= 1
    
    def __str__(self):
        current, stringify = self._virtual_head, []
        while current:
            stringify.append(current.value)
            current = current.next_node
        return '->'.join(str(value) for value in stringify)


if __name__ == '__main__':
    test_linked_list = SingleLinkedList()
    test_linked_list.add_at_head(1)
    test_linked_list.add_at_head(2)
    test_linked_list.add_at_head(3)
    test_linked_list.add_at_tail(4)
    test_linked_list.delete_at_index(4)
    print(test_linked_list)
