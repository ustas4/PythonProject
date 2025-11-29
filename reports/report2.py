import asyncio

class Report2:

    @classmethod
    async def do(cls):
        print('This is report 2')
        # time.sleep(1)
        await asyncio.sleep(5)
        print('report 2 done')