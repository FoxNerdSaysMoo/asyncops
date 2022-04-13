import asyncio
from asyncops import add, minus, divide, multiply


async def main():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    tasks = []
    for i in range(len(a)):
        tasks.append(asyncio.create_task(add(a[i], b[i])))
        tasks.append(asyncio.create_task(minus(a[i], b[i])))
        tasks.append(asyncio.create_task(multiply(a[i], b[i])))
        tasks.append(asyncio.create_task(divide(a[i], b[i])))
    await asyncio.gather(*tasks)
    print([i.result() for i in tasks])

if __name__ == '__main__':
    asyncio.run(main())
