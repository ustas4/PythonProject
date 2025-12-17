# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from local_file_picker import LocalFilePicker
from nicegui import ui

from reports.mediator import Mediator

async def pick_file() -> None:
    result = await LocalFilePicker('~', multiple=True)
    ui.notify(f'You chose {result}')

async def pick_file2(xi_mediator: Mediator) -> None:
    # Use a breakpoint in the code line below to debug your script.
    start_time = time.time()
    #  Create object of class Mediator. Response on collect of necessaries reports and run reports asynchronously
    xi_mediator.clean_all()
    #  User selected report 1, 2, 3
    await xi_mediator.create_callback_dictionary(1)
    await xi_mediator.create_callback_dictionary(2)
    await xi_mediator.create_callback_dictionary(3)
    # mediator.drop(3)
    # Run selected reports
    # print(mediator.selected_reports)
    # await xi_mediator.run_callback()
    end_time = time.time()
    print(f"\nTasks done in {end_time-start_time:.3f} sec")

async def run_reports(xi_mediator: Mediator):
    start_time = time.time()
    await xi_mediator.run_callback()
    end_time = time.time()
    print(f"\nTasks done in {end_time - start_time:.3f} sec")

@ui.page('/')
def index():
    mediator = Mediator()
    ui.button('Choose file', on_click= lambda: pick_file2(mediator), icon='folder')
    ui.button('Run reports', on_click= lambda : run_reports(mediator), icon='run')

# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # Ignore warning on never awaited coroutine reports
#     warnings.filterwarnings('ignore', category=RuntimeWarning)
ui.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
