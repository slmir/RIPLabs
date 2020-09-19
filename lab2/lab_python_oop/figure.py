from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def yardage(self):
        pass
