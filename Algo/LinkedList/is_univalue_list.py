from linked_list_module import Node


def is_univalue_list(head):
    value = head.val
    current = head.next
    while current is not None:
        if current.val != value:
            return False
        current = current.next
    return True


u = Node(2)
v = Node(2)
w = Node(2)
x = Node(2)
y = Node(2)

u.next = v
v.next = w
w.next = x
x.next = y

a = Node(7)
b = Node(7)
c = Node(4)

a.next = b
b.next = c

# 7 -> 7 -> 4
y = is_univalue_list(a)  # False
print(y, "y")

# 2 -> 2 -> 2 -> 2 -> 2

x = is_univalue_list(u)  # True
print(x)
