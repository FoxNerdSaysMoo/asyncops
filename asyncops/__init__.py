import asyncio
import functools
import contextvars


def _op(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        raise ValueError('Invalid operator')


async def to_thread(func, /, *args, **kwargs):
    """asyncio.to_thread, defined here for those who use <3.9"""
    loop = asyncio.get_running_loop()
    ctx = contextvars.copy_context()
    func_call = functools.partial(ctx.run, func, *args, **kwargs)
    return await loop.run_in_executor(None, func_call)


async def add(x, y):
    return await to_thread(_op, x, y, '+')


async def minus(x, y):
    return await to_thread(_op, x, y, '-')


async def multiply(x, y):
    return await to_thread(_op, x, y, '*')


async def divide(x, y):
    return await to_thread(_op, x, y, '/')