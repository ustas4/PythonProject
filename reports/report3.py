import asyncio

class Report3:

    @classmethod
    async def do(cls):
        print('This is report 3')
        # time.sleep(1)
        await asyncio.sleep(1)
        print('report 3 done')