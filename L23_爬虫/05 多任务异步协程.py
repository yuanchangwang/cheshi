# # 1.多任务异步协程
# import time
# import asyncio
#
#
# async def request(url):
#     print('正在下载: ', url)
#     time.sleep(2)   # time为非异步模块的代码,在此处如果存在非异步操作代码，则会彻底让asyncio失去异步的效果
#     print('下载成功:', url)
#
# start = time.time()
# urls = [
#     'www.baidu.com',
#     'www.taobao.com',
#     'www.sogou.com'
# ]
#
# loop = asyncio.get_event_loop()
#
# tasks = []  # 任务列表，放置多个任务对象
# for url in urls:
#     c = request(url)
#     task = asyncio.ensure_future(c)
#     tasks.append(task)
#
# # 将多个任务对象对应的列表注册到事件循环中
# loop.run_until_complete(asyncio.wait(tasks))
# print('总耗时: ', time.time()-start)


# # 1.多任务异步协程
# import time
# import asyncio
#
#
# async def request(url):
#     print('正在下载: ', url)
#     await asyncio.sleep(2)
#     print('下载成功:', url)
#
# start = time.time()
# urls = [
#     'www.baidu.com',
#     'www.taobao.com',
#     'www.sogou.com'
# ]
#
# loop = asyncio.get_event_loop()
#
# tasks = []  # 任务列表，放置多个任务对象
# for url in urls:
#     c = request(url)
#     task = asyncio.ensure_future(c)
#     tasks.append(task)
#
# # 将多个任务对象对应的列表注册到事件循环中
# loop.run_until_complete(asyncio.wait(tasks))
# print('总耗时: ', time.time()-start)


# # 使用真实的requests模块来发送请求
# import time
# import requests
# import asyncio
#
#
# async def get_page(url):
#     print('正在下载: ', url)
#     # 之所有没有实现异步操作，原因是requests是一个非异步的模块
#     response = requests.get(url=url)
#     print('响应数据', response.text)
#     print('下载成功:', url)
#
# start = time.time()
# urls = [
#     'http://127.0.0.1:5000/tiger',
#     'http://127.0.0.1:5000/jay',
#     'http://127.0.0.1:5000/tom',
# ]
# loop = asyncio.get_event_loop()
#
# tasks = []
# for url in urls:
#     c = get_page(url)
#     task = asyncio.ensure_future(c)
#     tasks.append(task)
#
# loop.run_until_complete(asyncio.wait(tasks))
# print('总耗时: ', time.time()-start)


# # 使用真实的requests模块来发送请求
# import time
# import asyncio
# import aiohttp
#
#
# async def get_page(url):
#     async with aiohttp.ClientSession() as session:
#         async with await session.get(url=url) as response:
#             page_text = await response.text()  # text()获取文本  read()获取二进制数据 json()
#             print(page_text)
#
# start = time.time()
# urls = [
#     'http://127.0.0.1:5000/tiger',
#     'http://127.0.0.1:5000/jay',
#     'http://127.0.0.1:5000/tom',
# ]
# loop = asyncio.get_event_loop()
#
# tasks = []
# for url in urls:
#     c = get_page(url)
#     task = asyncio.ensure_future(c)
#     tasks.append(task)
#
# loop.run_until_complete(asyncio.wait(tasks))
# print('总耗时: ', time.time()-start)

import time
import asyncio
import aiohttp

# 回调函数: 主要用来解析响应数据
def callback(task):
    print('This is callback')
    # 获取响应数据
    page_text = task.result()
    print("接下来就可以在回调函数中实现数据解析")

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        # 只要有耗时就会有阻塞，就得使用await进行挂起操作
        async with await session.get(url=url) as response:
            page_text = await response.text()  # 二进制read()/json()
            print('响应数据', page_text)
            return page_text

start = time.time()
urls = [
    'http://127.0.0.1:5000/tiger',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom',
]
loop = asyncio.get_event_loop()

tasks = []
for url in urls:
    cone = get_page(url)
    task = asyncio.ensure_future(cone)
    # 给任务对象绑定回调函数用于解析响应数据
    task.add_done_callback(callback)
    tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
print('总耗时: ', time.time()-start)