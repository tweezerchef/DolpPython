from linked_list_module import Node


a = Node(5)
b = Node(7)
c = Node(10)
d = Node(12)
e = Node(20)
f = Node(28)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 7 -> 10 -> 12 -> 20 -> 28

q = Node(6)
r = Node(8)
s = Node(9)
t = Node(25)
q.next = r
r.next = s
s.next = t


def merge_lists(head_1, head_2):
    if not head_1:
        return head_2
    if not head_2:
        return head_1

    dummy_node = Node(None)  # Dummy node to simplify the head handling
    tail = dummy_node

    current_1 = head_1
    current_2 = head_2

    while current_1 is not None and current_2 is not None:
        if current_1.val < current_2.val:
            tail.next = current_1
            current_1 = current_1.next
        else:
            tail.next = current_2
            current_2 = current_2.next
        tail = tail.next

    # Link the remaining elements
    if current_1:
        tail.next = current_1
    elif current_2:
        tail.next = current_2

    return dummy_node.next


x = merge_lists(a, q)
print(x)
