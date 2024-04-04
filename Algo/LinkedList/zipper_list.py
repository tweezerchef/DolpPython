from linked_list_module import Node

a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z


def zipper_lists(head_1, head_2):
    current_A = head_1
    current_B = head_2
    count = 0
    tail = head_1.next
    while current_A and current_B is not None:
        if count % 2 == 0:
            tail = current_A.next
            current_A.next = current_B
            count += 1
            current_A = tail
        else:
            tail = current_B.next
            current_B.next = current_A
            count += 1
            current_B = tail
    return head_1
