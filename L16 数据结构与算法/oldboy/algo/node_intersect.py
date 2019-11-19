# coding=utf-8
"""
author = jamon
"""

from algo.node import LinkedList


def check_loop(chain):
    has_loop, entry_node, loop_length, chain_length = False, None, 0, 0

    # Get header for fast and slow
    step = 0
    fast = slow = head = chain.header
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        step += 1
        # Note:
        # Do remember to use 'is' rather than '==' here (assure the id is same).
        if fast is slow:
            break
    has_loop = not(fast is None or fast.next is None)
    pass_length = (step * 2) if fast is None else (step * 2 + 1)

    if has_loop:
        step = 0
        while True:
            if head is slow:
                entry_node = slow
                pass_length = step
            if not entry_node:
                head = head.next
            fast = fast.next.next
            slow = slow.next
            step += 1
            if fast is slow:
                break
        loop_length = step

    chain_length = pass_length + loop_length
    return has_loop, entry_node, loop_length, chain_length


def check_intersect_one(c_1, c_2):
    def _traversal(c):
        node = c.header
        while node and node.next:
            yield node
            node = node.next
        yield node

    is_intersect, intersect_node = False, None
    # Get tail node and length
    step_1 = step_2 = 0
    for node_1 in _traversal(c_1):
        step_1 += 1
    for node_2 in _traversal(c_2):
        step_2 += 1
    tail_1, length_1 = node_1, step_1
    tail_2, length_2 = node_2, step_2

    if tail_1 is tail_2:
        # Intersected, fetch the first same node encountered as intersect node.
        is_intersect = True
        offset = length_1 - length_2
        long, short = (_traversal(c_1), _traversal(c_2)) if offset >= 0 else (_traversal(c_2), _traversal(c_1))
        for i in range(offset):
            next(long)
        for node_1, node_2 in zip(long, short):
            if node_1 is node_2:
                break
        intersect_node = node_1
    return is_intersect, intersect_node


def check_intersect_two(c_1, c_2):
    def _traversal(c):
        node = c.header
        while node and node.next:
            yield node
            node = node.next
        yield node

    # Create a loop for one of linked lists.
    for node in _traversal(c_1): pass
    node.next = c_1.header
    is_intersect, intersect_node = check_loop(c_2)[:2]
    # Un-loop
    node.next = None
    return is_intersect, intersect_node


if __name__ == '__main__':
    print('------------ intersect check ------------------')
    print('''
    chain_1:  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
    chain_2:  3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13
    ''')
    chain_1 = LinkedList(range(7))
    chain_2 = LinkedList(range(3, 14))
    print('Linked lists are intersected: %s, intersected node is: %s' % check_intersect_one(chain_1, chain_2))
    print('Linked lists are intersected: %s, intersected node is: %s' % check_intersect_two(chain_1, chain_2))

    # Merge two linked lists
    print('''Merge two linked lists:
    chain_1:  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 _
                                               \\
    chain_2:                 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13
    ''')
    node_6 = chain_1.find(6)
    node_7 = chain_2.find(7)
    node_6.next = node_7

    # Method one:
    print('Linked lists are intersected: %s, intersected node is: %s' % check_intersect_one(chain_1, chain_2))
    # Method two:
    print('Linked lists are intersected: %s, intersected node is: %s' % check_intersect_two(chain_1, chain_2))
