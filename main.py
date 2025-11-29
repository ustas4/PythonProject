# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import asyncio
import warnings
from reports.mediator import Mediator

async def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    start_time = time.time()
    #  Create object of class Mediator. Response on collect of necessaries reports and run reports asynchronously
    mediator = Mediator()
    mediator.clean_all()
    #  User selected report 1, 2, 3
    mediator.create_callback_dictionary(1)
    mediator.create_callback_dictionary(2)
    mediator.create_callback_dictionary(3)
    mediator.drop(3)
    # Run selected reports
    # print(mediator.selected_reports)
    await mediator.run_callback()
    end_time = time.time()
    print(f"\nTasks done in {end_time-start_time:.3f} sec")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ignore warning on never awaited coroutine reports
    warnings.filterwarnings('ignore', category=RuntimeWarning)
    asyncio.run(print_hi('PyCharm'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
