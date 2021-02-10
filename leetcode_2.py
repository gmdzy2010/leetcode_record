class ListNode:
    """A single link list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(link_1, link_2):
    head = walk = ListNode()
    carry = 0
    
    # loop the two link-list.
    while link_1 or link_2:
        if not link_1:
            total = link_2.val + carry
            link_2 = link_2.next
        elif not link_2:
            total = link_1.val + carry
            link_1 = link_1.next
        else:
            total = link_1.val + link_2.val + carry
            link_1, link_2 = link_1.next, link_2.next
        
        remainder, carry = total % 10, total // 10
        new = ListNode(remainder)
        walk.next = new
        walk = new
    
    if carry:
        extra_carry = ListNode(1)
        walk.next = extra_carry
    
    return head.next


if __name__ == '__main__':
    list_1 = [3, 0, 4]
    list_2 = [9, 9, 8, 1, 3]
    
    head_1 = cursor_1 = ListNode()
    head_2 = cursor_2 = ListNode()
    for element in list_1:
        new_node = ListNode(element)
        cursor_1.next = new_node
        cursor_1 = cursor_1.next
    for element in list_2:
        new_node = ListNode(element)
        cursor_2.next = new_node
        cursor_2 = cursor_2.next
    
    final_link_list = add_two_numbers(head_1.next, head_2.next)
    while final_link_list:
        print(final_link_list.val)
        final_link_list = final_link_list.next
