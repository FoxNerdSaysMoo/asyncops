# AsyncOps
## The async module you never knew you needed

Here at AsyncOps, we believe that everything should be async. Recently we realized that one crucial feature of async 
programming is missing- basic math operations. We've been working on a solution for this problem for a while, and that
is AsyncOps.

## Installation

```shell
$ pip install asyncops
```

## Usage

Feel free to look at the [examples](examples/basic.py)!

```python
import asyncops
import asyncio


async def main():
    print(await asyncops.add(1, 2))
    print(await asyncops.subtract(1, 2))
    print(await asyncops.multiply(1, 2))
    print(await asyncops.divide(1, 2))

asyncio.run(main())
```


