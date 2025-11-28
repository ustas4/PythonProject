# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import asyncio
from reports import *


async def session(report):
    await report

async def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    start_time = time.time()
    list_of_reports = [report1.Report1.do(), report2.Report2.do(), report3.Report3.do()]
    tasks = [session(report) for report in list_of_reports]
    await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"\nTasks done in {end_time-start_time:.3f} sec")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(print_hi('PyCharm'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
