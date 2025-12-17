import asyncio

from nicegui import ui
from reports.basereport import BaseReport
from local_file_picker import LocalFilePicker


class Report1(BaseReport):
    id = 1
    descriptor = 'Report do something'
    _selected_file: str

    def __init__(self, session):
        print(f'This is report initialization')
        super().__init__()
        self._session = session

    @classmethod
    async def do(cls, argument):
        await asyncio.sleep(1)
        print(f'This is {cls.name()} with argument: {argument} and {cls._selected_file}')

    @classmethod
    def name(cls):
        return f'{cls.id}. {cls.descriptor}'

    @classmethod
    async def cascade(cls, argument):
        print(f'This is cascade {cls.name()}')
        # await asyncio.sleep(5)
        # return None
        cls._selected_file = await LocalFilePicker('~', multiple=False)
        ui.notify(f'You chose {cls._selected_file}')
        print(f'The cascade {cls.name()} done')