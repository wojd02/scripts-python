from abc import ABC, abstractmethod
class Interface(ABC):
    @abstractmethod
    def executar(self):
        pass
