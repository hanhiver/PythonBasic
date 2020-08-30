import asyncio
from tornado.httpclient import AsyncHTTPClient

async def asynchronous_visit():
    http_client = AsyncHTTPClient()
    try:
        response = await http_client.fetch("http://www.baidu.com")
    except Exception as e:
        print("Error %s" % e)
    else:
        print(response)

async def print_progress():
    await asynchronous_visit()
    print("Progressing.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_progress())
    loop.close()