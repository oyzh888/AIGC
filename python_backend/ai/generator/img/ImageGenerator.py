from abc import abstractmethod
from abc import ABCMeta


class ImageGenerator(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def generate_img(cls, prompt, top_k):
        raise NotImplementedError