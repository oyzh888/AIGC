from abc import abstractmethod
from abc import ABCMeta


class TextGenerator(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def generate_text(cls, input_msg):
        raise NotImplementedError