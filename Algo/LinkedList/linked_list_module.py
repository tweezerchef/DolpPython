# linked_list_module.py


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create the linked list
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d


# Function to get the head of the list
def get_linked_list_head():
    return a
