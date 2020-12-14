# encoding:utf-8
import sys
import os
import time
import subprocess
import asyncio
import re
import functools
# import numpy as np
# import pandas as pd
# import os
# # def validate_age(a):
# #     return 18 <= a <= 30
# # https://lsp.readthedocs.io/en/latest/#cc

# # def level_b(s):
# #     return 60 <= s < 90

# print(os.getcwd())
# students = pd.read_excel("008/Students.xlsx", index_col=0)
# # print(students.head())
# # students = students.loc[students['Age'].apply(validate_age)]
# # .loc[students.Score.apply(level_b)]  # 两种语法
# print("*" * 60)
# print((students.loc[students['Age'].apply(
#     lambda x: 18 <= x <= 30)]))
# students = students.loc[students['Age'].apply(
#     lambda x: 18 <= x <= 30)].loc[students.Score.apply(lambda x: 60 <= x < 90)]
# print(students)

# arr2d = np.arange(12).reshape(3, 4)
# np.ndim(arr2d)
# print(arr2d)
# print(f'arr2d is ndim = {arr2d.ndim}')

# rd_arr = np.random.randn()
# print(rd_arr)

# rd_ar2d = np.random.randn(5, 3)
# print(rd_ar2d)
# ar = np.arange(12)
# ar2 = np.reshape(ar, (3, 4))
# print(ar2)


# class mymeta(type):
#     def __init__(self, a, b, c):
#         print(self)
#         print(a)
#         print(c)
#         print(b)

#     def __call__(self, *args, **kwargs):
#         obj = object.__new__(Foo)
#         self.__init__(obj, *args, **kwargs)
#         return obj


# class Foo(metaclass=mymeta):
#     def __init__(self, name):
#         self.name = name
#         print(self.name)


# foo = Foo("Python")
# print(foo.__dict__)
# print('---------------------------')


# class obj_slice(object):
#     def __init__(self):
#         self.cache = [1, 2, 3, 4, 5, 6, 7]

#     def __setitem__(self, key, value):
#         if isinstance(key, slice):
#             self.cache[key] = value

#     def __getitem__(self, key):
#         print("__getitem__ ", type(key))
#         print(
#             f"key.start={key.start} key.stop = {key.stop} key.step={key.step}")
#         return self.cache[key]

#     def __delitem__(self, key):
#         pass


# ob = obj_slice()
# ob[0:4:2] = ['a', 'b']
# print(ob[0:5:2])
# print(ob.__dict__)


# async def fn1():
#     print('1')
#     await asyncio.sleep(2)
#     print('2')
#     return 'coroutine is end'


# async def main1():
#     print('Main thread is start')
#     tasks_list = [
#         asyncio.create_task(fn1()),
#         asyncio.create_task(fn1())  # add to event loop
#     ]
#     print('Main thread is end')
#     done, pending = await asyncio.wait(tasks_list)
#     print(done)


# if __name__ == "__main__":
#     asyncio.run(main1())


# async def coro_fn1():
#     print("first is 1")
#     await asyncio.sleep(1)
#     print("second is 2")


# co_fn1 = coro_fn1()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(co_fn1)  # --> asyncio.run(coroutin object)


# async def set_after(fut, delay, value):
#     # Sleep for *delay* seconds.
#     await asyncio.sleep(delay)

#     # Set *value* as a result of *fut* Future.
#     fut.set_result(value)
#     print(f'value = {value}')


# async def main():
#     # Get the current event loop.
#     loop = asyncio.get_running_loop()

#     # Create a new Future object.
#     fut = loop.create_future()

#     # Run "set_after()" coroutine in a parallel Task.
#     # We are using the low-level "loop.create_task()" API here because
#     # we already have a reference to the event loop at hand.
#     # Otherwise we could have just used "asyncio.create_task()".
#     loop.create_task(set_after(fut, 1, '... world'))

#     print('hello ...')

#     # Wait until *fut* has a result (1 second) and print it.
#     print(await fut)

# # asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([main()]))


# async def get_date():
#     code = 'import datetime; print(datetime.datetime.now())'

#     # Create the subprocess; redirect the standard output
#     # into a pipe.
#     proc = await asyncio.create_subprocess_exec(
#         sys.executable, '-c', code,
#         stdout=asyncio.subprocess.PIPE)

#     # Read one line of output.
#     data = await proc.stdout.readline()
#     line = data.decode('ascii').rstrip()

#     # Wait for the subprocess exit.
#     await proc.wait()
#     return line


# async def run(cmd):
#     proc = await asyncio.create_subprocess_exec(
#         cmd, "127.0.0.1",
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE)
#     # loop = asyncio.get_running_loop()
#     # task1 = loop.create_task(proc.communicate())
#     stdout, stderr = await proc.communicate()
#     # await task1
#     print(f'[{cmd!r} exited with {proc.returncode}]')
#     if stdout:
#         print(f'[stdout]\n{stdout.decode("gbk")}')
#     if stderr:
#         print(f'[stderr]\n{stderr.decode("gbk")}')
#     print('safe exit')

# if __name__ == "__main__":
#     if sys.platform == "win32":
#         asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
#     # date = asyncio.run(get_date())
#     # print(f"Current date: {date}")

#     asyncio.run(run("ping"))

# https://zhuanlan.zhihu.com/p/266038260 sbuprocess


# async def ping(last_octect):
#     ip = '172.16.1.%s' % last_octect
#     await asyncio.create_subprocess_exec('ping', '-n', '1', '-w', '1', ip,
#                                          stdout=asyncio.subprocess.PIPE)


# async def main():
#     tasks = []
#     for i in range(1, 255):
#         tasks.append(ping(i))
#     loop = asyncio.get_running_loop()
#     task1 = loop.create_task(tasks)
#     # await asyncio.wait(tasks)
#     await task1


# if __name__ == "__main__":
#     if sys.platform == "win32":
#         asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
#     start_time = time.time()
#     loop = asyncio.ProactorEventLoop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(main())
#     loop.close()
#     print('总共耗时: %.2f' % (time.time()-start_time))


# async def ping1(last_octect):
#     ip = '172.16.1.%s' % last_octect
#     await asyncio.create_subprocess_exec('ping', '-n', '1', '-w', '1', ip,
#                                          stdout=asyncio.subprocess.PIPE)


# async def main():
#     tasks = []
#     for i in range(1, 255):
#         tasks.append(ping1(i))
#     await asyncio.wait(tasks)
#     # loop = asyncio.get_running_loop()
#     # task = loop.create_task(ping(12))
#     # await tasks

# if __name__ == "__main__":
#     if sys.platform == "win32":
#         asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
#     start_time = time.time()
#     loop = asyncio.ProactorEventLoop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(main())
#     loop.close()
#     asyncio.run(main())
#     print('总共耗时: %.2f' % (time.time()-start_time))

# @asyncio.coroutine
# def create_subprocess_exec(program, *args, stdin=None, stdout=None,
#                            stderr=None, loop=None,
#                            limit=asyncio.streams._DEFAULT_LIMIT, **kwds):
#     if loop is None:
#         loop = asyncio.events.get_event_loop()
#     def protocol_factory(): return asyncio.SubprocessStreamProtocol(limit=limit,
#                                                             loop=loop)
#     transport, protocol = yield from loop.subprocess_exec(
#         protocol_factory,
#         program, *args,
#         stdin=stdin, stdout=stdout,
#         stderr=stderr, **kwds)
#     return asyncio.Process(transport, protocol, loop)


# @asyncio.coroutine
# async def sleep(delay, result=None, *, loop=None):
#     """Coroutine that completes after a given time (in seconds)."""
#     if delay == 0:
#         yield
#         return result

#     if loop is None:
#         loop = asyncio.events.get_event_loop()
#     future = loop.create_future()
#     h = future._loop.call_later(delay,
#                                 futures._set_result_unless_cancelled,
#                                 future, result)
#     try:
#         return (yield from future)
#     finally:
#         h.cancel()
# asyncio.run(sleep())


# @asyncio.coroutine
# def ping(loop, target, dump=False):
#     create = asyncio.create_subprocess_exec('ping', target,
#                                             stdout=asyncio.subprocess.PIPE)
#     proc = yield from create
#     lines = []
#     while True:
#         line = yield from proc.stdout.readline()
#         if line == b'':
#             break
#         ch = line.decode('gbk').rstrip()
#         # print(f'ch is result = {ch}')
#         if dump:
#             print(ch)
#         lines.append(ch)
#         print(f'lines is content = {(lines)}')
#     transmited, received = [int(a.split(' ')[0]) for a
#                             in lines[-1].split(',')[:1]]
#     stats, unit = lines[-1].split(' = ')[-1].split(' ')
#     min_, avg, max_, stddev = [float(a) for a in stats.split('/')]
#     return transmited, received, unit, min_, avg, max_, stddev


# if __name__ == '__main__':
#     # loop = asyncio.get_event_loop()
#     # ping = loop.run_until_complete(ping(loop, 'free.txt'))
#     loop = asyncio.ProactorEventLoop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(ping(loop, "127.0.0.1"))
#     # print(ping)

#     loop.close()

# https://cloud.tencent.com/developer/article/1623049

# async def ping_call(num):
#     # 当前时间
#     current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#     ip = "192.168.31.%s  " % num
#     # 超时时间为1秒，ping 1次
#     cmd = 'ping -c 1 -w 1 -W 1 %s  ' % ip
#     print(cmd)
#     # 执行命令
#     proc = await asyncio.create_subprocess_exec('ping', '-c', '1', '-w', '1',
#                                                 '-W', '1', ip, stdout=asyncio.subprocess.PIPE)
#     # print("proc",proc,type(proc))
#     result = await proc.stdout.read()

#     # 通过正则匹配是否有100%关键字
#     regex = re.findall('100% packet loss', result.decode('gbk'))  # utf-8
#     # 长度为0时，表示没有出现100% packet loss
#     if len(regex) == 0:
#         return current_time, ip, True
#     else:
#         return current_time, ip, False


# async def main():  # 调用方
#     tasks = []
#     for i in range(1, 256):
#         # 把所有任务添加到task中
#         tasks.append(ping_call(i))

#     # 子生成器
#     # event_loop = asyncio.get_running_loop()
#     # obj = event_loop.create_task(tasks)
#     # done, pending = await obj
#     done, pending = await asyncio.wait(tasks)
#     # done和pending都是一个任务，所以返回结果需要逐个调用result()
#     for r in done:
#         # print(r.result())
#         # 判断布尔值
#         if r.result()[2]:
#             # 颜色代码
#             color_code = 32
#         else:
#             color_code = 31

#         info = "\033[1;{};1m{}\033[0m".format(color_code, r.result())
#         print(info)


# if __name__ == '__main__':
#     start = time.time()
#     # 创建一个事件循环对象loop
#     # loop = asyncio.get_event_loop()
#     loop = asyncio.ProactorEventLoop()
#     asyncio.set_event_loop(loop)
#     try:
#         # 完成事件循环，直到最后一个任务结束
#         # loop.run_until_complete(main())
#         loop.run_until_complete(main())
#     finally:
#         # 结束事件循环
#         loop.close()
#     print('所有IO任务总耗时%.5f秒' % float(time.time() - start))


# async def ping(prefix, ip):  # successfuly
#     # Create the subprocess; redirect the standard output
#     # into a pipe.
#     proc = await asyncio.create_subprocess_exec(
#         'ping', ip,  # 'ping', '-c', '4', 'www.baidu.com'
#         stdout=asyncio.subprocess.PIPE)

#     async for data in proc.stdout:
#         # print(f'data type = {type(data)}')
#         line = data.decode('gbk').rstrip()
#         # print(f'line type = {type(line)}')
#         print(prefix + line)

#     # Wait for the subprocess exit.
#     done = await proc.wait()
#     print(f'done = {done}')


# async def main():
#     await asyncio.gather(ping('1> ', 'www.baidu.com'), ping('2> ', "127.0.0.1"))

# # For Windows
# # https://stackoverflow.com/a/53146484/8810271
# loop = asyncio.ProactorEventLoop()
# asyncio.set_event_loop(loop)
# loop.run_until_complete(main())
# asyncio.run(main())


# this works

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# # this doesn't


# async def test_async(num):
#     print('Task #{0} start'.format(num))

#     proc = await asyncio.create_subprocess_shell(
#         'dir',
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE,
#         stdin=asyncio.subprocess.PIPE)

#     stdout, stderr = await proc.communicate()
#     cmd = 'python'
#     print(f'[{cmd!r} exited with {proc.returncode}]')
#     if stdout:
#         print(f'[stdout]\n{stdout.decode("gbk")}')
#     if stderr:
#         print(f'[stderr]\n{stderr.decode("gbk")}')
#     # await proc.wait()


# async def test_loop():
#     task1 = asyncio.create_task(
#         test_async(1))

#     task2 = asyncio.create_task(
#         test_async(2))

#     print(f"started at {time.strftime('%X')}")

#     await task1
#     await task2

#     print(f"finished at {time.strftime('%X')}")


# if __name__ == "__main__":
#     loop = asyncio.ProactorEventLoop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(test_loop())
#     loop.close()
# asyncio.run(test_loop()) # windows error must be up 3 statment

# def main():
#     if os.name == 'nt':
#         loop = asyncio.ProactorEventLoop()
#         asyncio.set_event_loop(loop)
#     else:
#         loop = asyncio.get_event_loop()
#     loop.run_until_complete(start(
#         'sleep 2; wc', input=[b'foo bar baz\n'*300 for i in range(100)]))
#     loop.close()
# main()


# async def coroutine_example():
#     await asyncio.sleep(1)
#     return 'zhihu ID: Zarten'

# coro = coroutine_example()

# loop = asyncio.get_event_loop()
# task = loop.create_task(coro)
# print('运行情况：', task)
# try:
#     print('返回值：', task.result())
# except asyncio.InvalidStateError:
#     print('task状态未完成，捕获了 InvalidStateError 异常')

# loop.run_until_complete(task)
# print('再看下运行情况：', task)
# print('返回值：', task.result())
# loop.close()

# http://www.voidcn.com/article/p-cquzfkbw-brh.html
# import requests
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# from threading import current_thread
# import time
# import os


# def get(url):
#     print('%s GET %s' % (os.getpid(), url))
#     response = requests.get(url)
#     time.sleep(3)
#     if response.status_code == 200:
#         return {'url': url, 'text': response.text}


# def parse(obj):
#     res = obj.result()
#     print('[%s] <%s> (%s)' % (os.getpid(), res['url'], len(res['text'])))


# if __name__ == '__main__':
#     urls = [
#         'https://www.python.org',
#         'https://www.baidu.com',
#         'https://www.jd.com',
#         'https://www.tmall.com',
#     ]
#     t = ProcessPoolExecutor(2)
#     for url in urls:
#         t.submit(get, url).add_done_callback(parse)
#     t.shutdown(wait=True)

#     print('主', os.getpid())


# async def set_after(fut, delay, value):
#     # Sleep for *delay* seconds.
#     await asyncio.sleep(delay)

#     # Set *value* as a result of *fut* Future.
#     fut.set_result(value)


# async def main():
#     # Get the current event loop.
#     loop = asyncio.get_running_loop()

#     # Create a new Future object.
#     fut = loop.create_future()

#     # Run "set_after()" coroutine in a parallel Task.
#     # We are using the low-level "loop.create_task()" API here because
#     # we already have a reference to the event loop at hand.
#     # Otherwise we could have just used "asyncio.create_task()".
#     loop.create_task(
#         set_after(fut, 1, '... world'))

#     print('hello ...')

#     # Wait until *fut* has a result (1 second) and print it.
#     # print(await fut)
#     res = await fut
#     print(f'res = {res}')

# asyncio.run(main())


# def my_callback(task, future):
#     print('返回值：', future.result())
#     print(f'task={type(task)} future={type(future)}')
#     return future.result()


# async def coroutine_example():
#     await asyncio.sleep(1)
#     return 'zhihu ID: Zarten'


# async def main():
#     loop = asyncio.get_running_loop()
#     fu = loop.create_future()
#     coro = coroutine_example()
#     task = loop.create_task(coro)
#     task.add_done_callback(functools.partial(my_callback, fu))
#     res = await task
#     print(f'res = {res}')

# asyncio.run(main())


