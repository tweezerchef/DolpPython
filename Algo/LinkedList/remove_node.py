def remove_node(head, target_val):
    if head is None:
        return None

    while head is not None and head.val == target_val:
        head = head.next

    current = head
    prev = None
    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            current = current.next
            break
        else:
            prev = current
            current = current.next

    return head
