from abc import ABC, abstractmethod

# Define the abstract base class (inherits from ABC)
class BaseReport(ABC):

    @classmethod
    @abstractmethod
    async def do(cls):
        """Abstract method that must be implemented by subclasses."""
        pass

    @classmethod
    @abstractmethod
    async def cascade(cls):
        """Abstract method that must be implemented by subclasses."""
        pass
    @property
    @abstractmethod
    def id(self) -> int:
        """The id of the report."""
        pass

    @property
    @abstractmethod
    def descriptor(self) -> int:
        """The descriptor of the report."""
        pass
    def name(self):
        """A concrete method that can be inherited or overridden."""
        print(f"{self.id}. {self.descriptor}")
# # Define a concrete subclass
# class Car(Vehicle):
#     def drive(self):
#         """Implement the abstract drive method for a Car."""
#         print("The car is driving.")
#
# # Define another concrete subclass
# class Motorcycle(Vehicle):
#     def drive(self):
#         """Implement the abstract drive method for a Motorcycle."""
#         print("The motorcycle is driving.")
#
# # --- Usage ---
#
# # This would raise a TypeError because abstract classes cannot be instantiated
# # try:
# #     abstract_vehicle = Vehicle()
# # except TypeError as e:
# #     print(f"Error: {e}")
#
# # Instantiate concrete subclasses
# my_car = Car()
# my_motorcycle = Motorcycle()
#
# # Call methods
# my_car.start()  # Inherited concrete method
# my_car.drive()  # Implemented abstract method
#
# my_motorcycle.start()
# my_motorcycle.drive()
