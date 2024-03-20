from linked_list_module import Node

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d


def get_node_value(head, index):
    pass  # todo
    current = head
    count = 0
    while current is not None:
        if index == count:
            return current.val
        count = count + 1
        current = current.next


print(get_node_value(a, 2))
print(get_node_value(a, 3))
