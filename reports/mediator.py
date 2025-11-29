from typing import Callable, Dict
import asyncio
# Below should be imported ALL reports
from reports.report1 import Report1
from reports.report2 import Report2
from reports.report3 import  Report3


async def session(report):
    await report


class Mediator:

    def __init__(self):
        #   Define a type hint for the callback function (a class method returning a string)
        self.callback_func = Callable[[], str]
        self.selected_reports = {}
        # self.all_callbacks contains all available reports (as exampled)
        self.all_callbacks: Dict[int, ()] = {1: Report1.do(), 2: Report2.do(), 3: Report3.do()}

    def create_callback_dictionary(self, choice: int) -> None:
        """
        Create a list containing the selected class method callback.
        :param choice: An integer  (1 or 2) corresponding to desired report class's do() method.
        :return: None
        """
        # Map all available class methods
        # Note: Report1.do() is passed as function reference (without parentheses)

        if choice in self.all_callbacks:
            # Collect list
            self.selected_reports[choice] = self.all_callbacks[choice]
        else:
            print(f"Invalid choice {choice}")

    def clean_all(self):
        self.selected_reports = {}

    def drop(self, list_dropped: list[int]) -> None:
        """
        Drop report form selected
        :param list_dropped:  list of indexes (keys)
        :return: None
        """
        if isinstance(list_dropped, int):
            list_dropped = [list_dropped]
        for each in list_dropped:
            removed_value = self.selected_reports.pop(each, None)
            if removed_value:
                print(f"Removed Report{each}.")

    async def run_callback(self):
        """
        Helper function to demonstrate running the function stored in the dictionary
        :param
        :return:
        """
        if not self.selected_reports:
            print("No callback function provided to run.")
            return
        list_of_reports = [*self.selected_reports.values()]
        tasks = [session(report) for report in list_of_reports]
        await asyncio.gather(*tasks)
        print("--------------------------------------------")

