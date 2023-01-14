from ai.generator.prompt import PromptGenerator

'''
Return input message as it is
'''
class DummyPromptGenerator(PromptGenerator):

    @classmethod
    def generate_prompt(cls, input_msg):
        return input_msg