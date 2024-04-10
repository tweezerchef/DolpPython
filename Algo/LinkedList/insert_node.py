from linked_list_module import Node


def insert_node(head, value, index):
    current = head
    prev = head
    count = 0
    if index == 0:
        head = Node(value)
        head.next = current
        return head
    while current is not None:
        if count == index:
            next = current
            value = Node(value)
            current = value
            prev.next = current
            current.next = next
            break
        elif current.next is None:
            count += 1
            if count == index:
                current.next = Node(value)
                break
            else:
                break
        else:
            prev = current
            current = current.next
            count += 1
    return head


# simpler solution
def insert_node_1(head, value, index):
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    count = 0
    current = head
    while current is not None:
        if count == index - 1:
            temp = current.next
            current.next = Node(value)
            current.next.next = temp

        count += 1
        current = current.next
    return head
