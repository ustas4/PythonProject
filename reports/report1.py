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

# import asyncio
# from abc import ABC
#
# from nicegui import ui
#
# from local_file_picker import LocalFilePicker
# from reports.abc_report import AbcReport
#
#
# class Report1(AbcReport, ABC):
#     self._id = 1
#     self._descriptor = 'Report do something'
#     def __init__(self):
#         super().__init__()
#         self._id = 1
#         self._descriptor = 'Report do something'
#         # self.cascade()
#
#     async def do(self):
#         print(f'This is report {self.name()}')
#         # time.sleep(1)
#         await asyncio.sleep(5)
#         print(f'The report {self.name()} done')
#
#     async def cascade(self):
#         print(f'This is cascade {self.name()}')
#         await asyncio.sleep(5)
#         # result = await LocalFilePicker('~', multiple=False)
#         # ui.notify(f'You chose {result}')
#         print(f'The cascade {self.name()} done')
#
#
#     @property  # 1. Getter MUST come first
#     def id(self):
#         return self._id
#
#     @id.setter
#     def id(self, value):
#         self._id = value
#
#     @property
#     def descriptor(self):
#         return self._descriptor
#
#     @descriptor.setter
#     def descriptor(self, value):
#         self._descriptor = value