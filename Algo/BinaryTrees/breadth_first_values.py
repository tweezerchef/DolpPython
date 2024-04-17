from collections import deque
from binary_tree_module import Node


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def breadth_first_values(root):
    queue = deque()
    queue.append(root)
    output = []
    while queue:
        current = queue.popleft()
        output.append(current.val)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return output


x = breadth_first_values(a)
print(x)
