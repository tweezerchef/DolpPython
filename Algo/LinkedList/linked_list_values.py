# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d


def linked_list_values(head):
    pass  # todo
    output_arr = []
    while head is not None:
        output_arr.append(head.val)
        head = head.next

    return output_arr


output = linked_list_values(a)

print(output)
