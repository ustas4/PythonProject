import asyncio

from nicegui import ui
from reports.basereport import BaseReport


class Report2(BaseReport):
    id = 2
    descriptor = 'Report do something other'
    _selected_file2: str

    def __init__(self, session):
        print(f'This is report initialization')
        super().__init__()
        self._session = session

    @classmethod
    async def do(cls, argument):
        await asyncio.sleep(1)
        print(f'This is {cls.name()} with argument: {argument} and {cls._selected_file2}')

    @classmethod
    def name(cls):
        return f'{cls.id}. {cls.descriptor}'

    @classmethod
    async def cascade(cls, argument):
        print(f'This is cascade {cls.name()}')
        await asyncio.sleep(5)
        # return None
        cls._selected_file2 = 'any variable'
        ui.notify(f'You chose {cls._selected_file2}')
        print(f'The cascade {cls.name()} done')
