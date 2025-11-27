from abc import ABC, abstractmethod


class BaseCategory(ABC):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self):
        pass
