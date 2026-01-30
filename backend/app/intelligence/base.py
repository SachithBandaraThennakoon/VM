from abc import ABC, abstractmethod

class IntelligenceModule(ABC):

    @abstractmethod
    def evaluate(self, inputs: dict) -> dict:
        """
        Takes abstract student state and returns guidance signals.
        """
        pass
