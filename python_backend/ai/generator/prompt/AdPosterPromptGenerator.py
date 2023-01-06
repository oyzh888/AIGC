from ai.generator.prompt import PromptGenerator

class AdPosterPromptGenerator(PromptGenerator):

    @classmethod
    def generate_prompt(cls, input_msg):
        return "Write a stunning and attractive paragraph for advertisement poster based on the keywords below: \n\n" + "\n\n" \
                 + input_msg + "\n\n"