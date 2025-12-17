import asyncio

from nicegui import ui
from reports.basereport import BaseReport


class Report3(BaseReport):
    id = 3
    descriptor = 'Report do something other'

    def __init__(self, session):
        print(f'This is report initialization')
        super().__init__()
        self._session = session

    @classmethod
    async def do(cls, argument):
        await asyncio.sleep(1)
        print(f'This is {cls.name()} with argument: {argument}')

    @classmethod
    def name(cls):
        return f'{cls.id}. {cls.descriptor}'

    @classmethod
    async def cascade(cls, argument):
        print(f'This is cascade {cls.name()}')
        await asyncio.sleep(0.1)
        ui.notify(f'cascade passed')
