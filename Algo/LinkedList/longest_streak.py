from linked_list_module import Node


def longest_streak(head):
    if head is None:
        return 0
    current = head
    record = 1
    count = 1
    while current.next is not None:
        if current.val == current.next.val:
            count += 1
            if count > record:
                record = count
        else:
            count = 1
        current = current.next
    return record


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

x = longest_streak(a)  # 4
print(x)
