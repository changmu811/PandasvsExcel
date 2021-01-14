# import pandas as pd
# import numpy as np

# frame_11 = pd.DataFrame({'a': range(4), 'b': range(
#     4, 0, -1), 'c': ['one', 'one', 'two', 'two'], 'd': [0, 1, 2, 3]})
# print(frame_11)
# frame_12 = frame_11.set_index(['c', 'd'])
# print(frame_12)
# frame_13 = frame_11.set_index(['c', 'd'], drop=False)
# print(frame_13)
# print(frame_12.reset_index())
# frame_14 = frame_11.set_index(['c', 'd'], drop=False, append=True)
# print(frame_14)
# print('--' * 50)
# stocks = pd.DataFrame(np.arange(1, 17).reshape(4, 4),  columns=[
#     ['京东', '京东', '天猫', '天猫'], ['price', 'number', 'price', 'number']])
# print(stocks)
# print(stocks.columns)
# print(stocks.index)
# print(stocks.values)
# print(stocks['京东', 'number'])
# print('->' * 40)
# mux = pd.MultiIndex.from_product([list('ab'), [2014, 2015], range(1, 3)])
# df = pd.DataFrame(dict(A=1), mux)
# print(df)
# print(df.index.get_level_values(0))
# df.index.map('{0[2]}/{0[1]}'.format)
# df.index = [df.index.get_level_values(0), df.index.map('{0[2]}/{0[1]}'.format)]
# print(df)


# frame = pd.DataFrame(np.arange(12).reshape(4, 3),
#                      index=[list('aabb'), list('1212')],
#                      columns=[['ohio', 'ohio', 'colorado'], ['Green', 'Red', 'Green']])
# print(frame)


# import asyncio
# import sys


# async def main():
#     await asyncio.gather(
#         myrun('dir'),
#         myrun('dir *.*'))


# async def myrun(cmd):
#     proc = await asyncio.create_subprocess_shell(
#         cmd,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE)

#     stdout, stderr = await proc.communicate()

#     print(f'[{cmd!r} exited with {proc.returncode}]')
#     if stdout:
#         print(f'[stdout]\n{stdout.decode("gbk")}')
#     if stderr:
#         print(f'[stderr]\n{stderr.decode("gbk")}')
# if __name__ == '__main__':
#     # asyncio.run(myrun('dir'))
#     if sys.platform == 'win32':
#         loop = asyncio.ProactorEventLoop()
#         asyncio.set_event_loop(loop)
#         loop.run_until_complete(main())
#         loop.close()
#     else:
#         print('Runing error')
#     # asyncio.run(test_loop())
#     # asyncio.windows_events.ProactorEventLoop


# async def myping(last_octect):
#     ip = '172.16.1.%s' % last_octect
#     proc = await asyncio.create_subprocess_exec('ping', '-n', '1', '-w', '1', ip, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, loop=loop)
#     stdout, stderr = proc.communicate()


# async def main():
#     tasks = []
#     for i in range(1, 255):
#         tasks.append(myping(i))
#     await asyncio.wait(tasks)


# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.ProactorEventLoop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(main())
#     print('总共耗时: %.2f' % (time.time()-start_time))
#     # loop.close()


import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    print(f'reader is type = {type(reader)}')
    print(f'writer is type = {type(writer)}')
    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


if __name__ == '__main__':
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(tcp_echo_client('hee koo'))



