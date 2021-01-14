# import pandas as pd
# import matplotlib.pyplot as plt

# users = pd.read_excel('C:/Temp/Users.xlsx')
# users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
# users.sort_values(by='Total', inplace=True, ascending=False)
# print(users)

# users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True)
# plt.tight_layout()
# plt.show()


# import asyncio
# import concurrent.futures


# def blocking_io():
#     # File operations (such as logging) can block the
#     # event loop: run them in a thread pool.
#     with open('e:/program/010keymaker.exe', 'rb') as f:
#         return f.read(100)


# def cpu_bound():
#     # CPU-bound operations will block the event loop:
#     # in general it is preferable to run them in a
#     # process pool.
#     return sum(i * i for i in range(10 ** 7))


# async def main():
#     loop = asyncio.get_running_loop()

#     # Options:

#     # 1. Run in the default loop's executor:
#     result = await loop.run_in_executor(
#         None, blocking_io)
#     print(f'result is type = {type(result)}')
#     print('default thread pool', result)

#     # 2. Run in a custom thread pool:
#     with concurrent.futures.ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(
#             pool, blocking_io)
#         print(f'pool is type = {type(pool)}  result is type = {type(result)}')
#         print('custom thread pool', result)

#     # 3. Run in a custom process pool:
#     with concurrent.futures.ProcessPoolExecutor() as pool:
#         result = await loop.run_in_executor(
#             pool, cpu_bound)
#         print(f'pool is type = {type(pool)}  result is type = {type(result)}')
#         print('custom process pool', result)
# if __name__ == "__main__":
#     asyncio.run(main())
#


import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    print(f'data is type = {type(reader.read)}')
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)
    print(f'server is type = {type(server)}')
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    # print(f'Get host of name = {server.sockets[0].getpeername()}')
    async with server:
        await server.serve_forever()

asyncio.run(main())
