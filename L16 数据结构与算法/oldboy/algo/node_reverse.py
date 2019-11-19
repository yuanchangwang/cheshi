# coding=utf-8
"""
author = jamon
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linkedlist1(head):
    if head == None or head.next == None:  # 边界条件
        return head
    arr = []  # 空间消耗为n,n为单链表的长度
    while head:
        arr.append(head.val)
        head = head.next
    newhead = ListNode(0)
    tmp = newhead
    for i in arr[::-1]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return newhead.next


def reverse_linkedlist2(head):
    if head == None or head.next == None:  # 边界条件
        return head
    p1 = head  # 循环变量1
    p2 = head.next  # 循环变量2
    tmp = None  # 保存数据的临时变量
    while p2:
        tmp = p2.next
        p2.next = p1
        p1 = p2
        p2 = tmp
    head.next = None
    return p1


def create_ll(arr):
    pre = ListNode(0)
    tmp = pre
    for i in arr:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return pre.next


def print_ll(head):
    tmp = head
    result = []
    while tmp:
        result.append(tmp.val)
        tmp = tmp.next
    print(result)


a = create_ll(range(5))
print_ll(a)  # 0 1 2 3 4
a = reverse_linkedlist1(a)
print_ll(a)  # 4 3 2 1 0
a = reverse_linkedlist2(a)
print_ll(a)  # 0 1 2 3 4
