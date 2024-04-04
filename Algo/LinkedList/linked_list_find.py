from linked_list_module import Node

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d


def linked_list_find(head, value):
    while head.next is not None:
        if head.val == value:
            return True
        else:
            head = head.next
    return False


print(linked_list_find(a, "g"))
