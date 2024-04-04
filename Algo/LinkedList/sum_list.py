from linked_list_module import Node

# head = get_linked_list_head()
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e


def sum_list(head):
    sum = 0
    while head is not None:
        sum += head.val
        head = head.next
    return sum


out = sum_list(a)

print(out)
