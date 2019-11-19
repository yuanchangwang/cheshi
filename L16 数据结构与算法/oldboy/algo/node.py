# coding=utf-8
"""
author = jamon
"""


class Node:
    def __init__(self, val=None, nxt=None):
        self.value = val
        self.next = nxt

    def __str__(self):
        return str(self.value)


class LinkedList:
    """
    Linked list:
            node_1 -> node_2 -> node_3 -> node_4
    """

    def __init__(self, iterable=()):
        self.header = None
        if iterable:
            self.init(iterable)

    def __str__(self):
        def _traversal(self):
            node = self.header
            while node and node.next:
                yield node
                node = node.next
            yield node

        return '->'.join(map(lambda x: str(x), _traversal(self)))

    def init(self, iterable=()):
        # Note: use empty tuple rather than list to init iterable
        if not iterable:
            return
        self.header = Node(iterable[0])  # header value
        node = self.header
        for i in iterable[1:]:  # add all node
            node.next = Node(i)
            node = node.next

    def show(self):
        print(self)

    @property
    def length(self):
        if self.header is None:
            return 0
        node = self.header  # node pointer points to header
        i = 1
        while node.next:
            node = node.next  # node pointer move to next
            i += 1
        return i

    @property
    def is_empty(self):
        return self.header is None

    def clear(self):
        self.__init__()
        # self.header = None

    def append(self, item):
        self.insert(item, self.length)

    def find(self, item):
        node = self.header
        while node.next and node.value != item:
            node = node.next
        if node.value == item:
            return node
        return None

    def find_previous(self, item):
        node = self.header
        while node.next and node.next.value != item:
            node = node.next
        if node.next and node.next.value == item:
            return node
        return None

    def delete(self, item):
        '''
        node_1 -- X --> node_2 -----> node_3
            \                    /
             \                  /
              ------------------
        '''
        prev = self.find_previous(item)
        if prev:
            prev.next = prev.next.next

    def insert(self, item, index):
        '''
                ----> node_2 ---
               /                \
              /                  \
        node_1 -------  X  ---------> node_3

        '''
        if abs(index) > self.length:
            return
        if index < 0:
            self.insert(item, self.length + index + 1)
            return
        elif index == 0:
            self.insert(self.header.value, 1)
            self.header.value = item
            return
        node = self.header
        i = 0
        while i < index - 1:
            node = node.next
            i += 1
        n = node.next
        node.next = Node(item, n)


def test(li):
    print('Show linked list:')
    li.show()

    print('\nInit linked list:')
    li.init([1, 2, 3, 4, 5, 6, 'xd', 8, 9])
    li.show()

    print('\nInsert element:')
    li.insert('xxd', -3)
    li.show()

    print('\nAppend element:')
    li.append('10')
    li.show()

    e = 'xd'
    print('\nFind element:')
    x = li.find(e)
    print(x.value if x else x)
    print('\nFind previous element:')
    x = li.find_previous(e)
    print(x.value if x else x)

    print('\nDelete element:')
    li.delete('xd')
    li.show()

    print('\nFind element not exist:')
    x = li.find(e)
    print(x.value if x else x)

    print('\nInsert element to header:')
    li.insert('cc', 0)
    li.show()

    print('\nClear linked list:')
    li.clear()
    li.show()

    print('\nCurrent length: %s' % li.length)
    print('\nIs empty: %s' % li.is_empty)


if __name__ == '__main__':
    test(LinkedList())

