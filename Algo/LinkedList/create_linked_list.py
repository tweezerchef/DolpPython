from linked_list_module import Node


# create linked list from array of values and return head
def create_linked_list(values):
    if len(values) == 0:
        return
    head = Node(values.pop(0))
    current = head
    for value in values:
        current.next = Node(value)
        current = current.next

    return head
