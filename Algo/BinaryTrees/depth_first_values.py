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


# first attempt gets all values but not in order
def depth_first_values_1(root):
    stack = [root]
    result_list = []
    while len(stack) > 0:
        current = stack.pop()
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
        result_list.append(current.val)

    return result_list


# second attempt
def depth_first_values(root):
    if root is None:
        return []
    stack = [root]
    result_list = []
    while stack:
        current = stack.pop()
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
        result_list.append(current.val)
    return result_list


def depth_first_values_recursive(root):
    if root is None:
        return []
    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)
    return [root.val, *left_values, *right_values]


x = depth_first_values_recursive(a)
print(x)
