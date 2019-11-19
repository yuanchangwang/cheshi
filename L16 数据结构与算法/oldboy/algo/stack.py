# coding=utf-8
"""
author = jamon
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 创建一个空栈
s = Stack()
print(s.isEmpty())

s.push(4)
s.push('dog')
print(s.items)

import time
start_time = time.time()

# 注意是三重循环
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print("a, b, c: %d, %d, %d" % (a, b, c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")

