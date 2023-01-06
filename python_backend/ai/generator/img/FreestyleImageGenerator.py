from ai.generator.img import ImageGenerator, RecommendationBasedImageGenerator

DEBUG = False

class FreestyleImageGenerator(ImageGenerator):

    @classmethod
    def generate_img(cls, input_msg, top_k=1):
        if DEBUG:
            url = "https://lexica.art?q=0482ee68-0368-4eca-8846-5930db866b33"
        else:
            # Fall back to recommendation-based generator
            url = RecommendationBasedImageGenerator.generate_img(input_msg, top_k)
        return url