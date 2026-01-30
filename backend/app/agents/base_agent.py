from abc import ABC, abstractmethod

class BaseAgent(ABC):

    @abstractmethod
    def act(self, context: dict) -> dict:
        """
        Takes shared context and returns structured output.
        """
        pass
