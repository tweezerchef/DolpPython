from binary_tree_module import Node


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def tree_sum(root):
    if root is None:
        return 0
    stack = [root]
    sum = 0
    while stack:
        current = stack.pop()
        sum += current.val
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    return sum


x = tree_sum(a)
print(x)
