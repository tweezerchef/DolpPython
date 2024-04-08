def remove_node(head, target_val):
    # Handle the case where the list is empty
    if head is None:
        return None

    # Handle the case where the node to remove is at the head
    while head is not None and head.val == target_val:
        head = head.next

    # Now handle the case where the node to remove is in the middle or end
    current = head
    prev = None
    while current is not None:
        if current.val == target_val:
            # Skip the current node
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next

    return head
