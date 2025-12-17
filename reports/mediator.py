from typing import Callable, Dict
import asyncio

from reports.basereport import BaseReport
# Below should be imported ALL reports
from reports.report1 import Report1
from reports.report2 import Report2
from reports.report3 import Report3





class Mediator:

    def __init__(self):
        #   Define a type hint for the callback function (a class method returning a string)
        self.callback_func = Callable[[], str]
        self.selected_reports = {}
        self.selected_cascades = {}
        self.all_callbacks: Dict[int, ()] = {}
        self.all_reports: Dict[int, BaseReport] = {}
        self.argument = 'SPARK_SESSION'
        list_of_classes = [Report1, Report2, Report3]
        for each in list_of_classes:
            id_report = each.id
            obj = each(self.argument)
            self.all_reports[id_report] = obj
            self.all_callbacks[id_report] = each.do(self.argument)

    async def create_callback_dictionary(self, choice: int) -> None:
        """
        Create a list containing the selected class method callback.
        :param choice: An integer  (1 or 2) corresponding to desired report class's do() method.
        :return: None
        """
        # Map all available class methods
        # Note: Report1.do() is passed as function reference (without parentheses)

        if choice in self.all_callbacks:
            # Collect list
            self.selected_reports[choice] = self.all_reports[choice]
            await self.all_reports[choice].cascade(self.argument)
            return None
        else:
            print(f"Invalid choice {choice}")
            return None

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
        tasks = [report.do(self.argument) for report in list_of_reports]
        await asyncio.gather(*tasks)
        print("--------------------------------------------")