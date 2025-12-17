from abc import ABC, abstractmethod


# Define the abstract base class (inherits from ABC)
class BaseReport(ABC):

    @classmethod
    @abstractmethod
    async def do(cls, arg):
        """Abstract method that must be implemented by subclasses."""
        pass

    @classmethod
    @abstractmethod
    async def cascade(cls, arg):
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
