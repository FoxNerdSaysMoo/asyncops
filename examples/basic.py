from asyncops import *


async def main():
    print(await add(1, 2))
    print(await minus(1, 2))
    print(await multiply(1, 2))
    print(await divide(1, 2))


if __name__ == '__main__':
    asyncio.run(main())

