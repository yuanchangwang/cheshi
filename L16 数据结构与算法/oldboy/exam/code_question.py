# coding=utf-8
"""
author = jamon
"""

print(99.9 - 90)
print(99.9-90.9 == 9.0)
print(99.9-90.0 == 9.9)

# get_node_index = lambda x: int(x % 10)
# temp = [n for n in range(10)]
# for i in range(len(temp)):
#     if get_node_index(temp[i]):
#         del temp[i]
# print(temp)
#
#
# session_cache = [10000, 10001, 10002]
# def add_session(session_id):
#     session_cache.append(session_id)
#
# def add_session2(session_id):
#     session_cache += [session_id]
#
# add_session(10003)
# print(session_cache)
#
# add_session2(10004)
# print(session_cache)



# class A(object):
#     x = 1
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# print(A.x, B.x, C.x)
# B.x = 2
# print(A.x, B.x, C.x)
# A.x = 3
# print(A.x, B.x, C.x)



# def f(x, l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(2)
# f(3, [3, 2, 1])
# f(3)


# def test():
#     return [lambda x: i*x for i in range(5)]
# for ret in test():
#     print(ret(2))


# import b
# def f():
#     return b.x
# print(f())
#
# import a
# x=1
# def g():
#     print(a.f())


# a = 1
# try:
#     a += 1
# except:
#     a += 1
# else:
#     a += 1
# finally:
#     a += 1
# print(a)


# i = 5
# def f2(k=i):
#     print(k)
# i = 6
# f2()


temp = [[]]*3
temp[0].append(10)
temp[1].append(20)
temp[2].append(30)
print(temp)