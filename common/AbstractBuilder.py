from abc import ABC, abstractmethod


class AbstractBuilder(ABC):
    def __init__(self, from_entity=None):
        self.skip_validate = False
        self.entity = from_entity if from_entity else self.create_entity()

    @abstractmethod
    def create_entity(self):
        pass

    def skip_validate_(self):
        self.skip_validate = True
        return self

    def build(self):
        if not self.skip_validate:
            self.validate()
        return self.entity

    @abstractmethod
    def validate(self):
        pass
