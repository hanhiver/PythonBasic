import asyncio

async def ticker(delay, to):
    """
    Yield numbers from 0 to *to* every *delay* seconds. 
    """
    for i in range(to):
        yield i 
        await asyncio.sleep(delay)

if __name__ == '__main__':
    for i in ticker(1, 5):
        print(i)
        
