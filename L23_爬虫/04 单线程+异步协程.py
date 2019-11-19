

# # 基本使用
# import asyncio
#
# # 定义了一个特殊函数
# async def hello(name):
#     print("hello " + name)
#     # return "hello " + name
#
# # 通过函数名加括号执行这个特殊函数，并不会立即执行，而是返回一个协程对象
# c = hello("oldboy")
#
# # 实例化一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将协程对象注册到事件循环中, 并执行事件循环
# loop.run_until_complete(c)



# # task的使用
# import asyncio
#
# # 定义了一个特殊函数
# async def hello(name):
#     return "hello " + name
#
# # 通过函数名加括号执行这个特殊函数，并不会立即执行，而是返回一个协程对象
# c = hello("oldboy")
#
# # 实例化一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 创建一个task任务对象
# task = loop.create_task(c)
#
# # 将协程对象注册到事件循环中, 并执行事件循环
# print(task)
# loop.run_until_complete(task)
# print(task)



# # feture的使用
# import asyncio
#
# # 定义了一个特殊函数
# async def hello(name):
#     return "hello " + name
#
# # 通过函数名加括号执行这个特殊函数，并不会立即执行，而是返回一个协程对象
# c = hello("oldboy")
#
# # 实例化一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 创建一个feture任务对象
# feture = asyncio.ensure_future(c)
#
# # 将协程对象注册到事件循环中, 并执行事件循环
# print(feture)
# loop.run_until_complete(feture)
# print(feture)


# 回调函数的使用
import asyncio

# 定义了一个特殊函数
async def request(url):
    print("向URL发送请求，获取响应数据" + url)
    return "page_text"

# 定义一个回调函数，用来实现数据解析
def call_back(task):
    print("在这里进行数据解析操作")
    print(task.result())


# 通过函数名加括号执行这个特殊函数，并不会立即执行，而是返回一个协程对象
c = request("https://www.baidu.com")

# 实例化一个事件循环对象
loop = asyncio.get_event_loop()

# 创建一个feture任务对象
feture = asyncio.ensure_future(c)

# 加上一个绑定回调
feture.add_done_callback(call_back)

# 将协程对象注册到事件循环中, 并执行事件循环
loop.run_until_complete(feture)

