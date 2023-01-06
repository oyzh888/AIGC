from abc import abstractmethod
from abc import ABCMeta


class PromptGenerator(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def generate_prompt(cls, input_msg):
        raise NotImplementedError