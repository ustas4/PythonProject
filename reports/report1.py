import asyncio

class Report1:

    @classmethod
    async def do(cls):
        print('This is report 1')
        # time.sleep(1)
        await asyncio.sleep(1)
        print('report 1 done')