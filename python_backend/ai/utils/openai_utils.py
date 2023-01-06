import os
import openai

os.environ["OPENAI_API_KEY"] = "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"
# Shane
# os.environ["OPENAI_API_KEY"] = "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"

class OpenaiUtils:

    @classmethod
    def call_openai_text(cls, prompt_text, n_returns=1):
        output_texts = []
        openai.api_key = os.environ["OPENAI_API_KEY"]
        for _ in range(n_returns):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt_text,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            output_texts.append(response["choices"][0]["text"])
        return output_texts