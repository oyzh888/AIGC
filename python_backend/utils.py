

import time
import openai
import os
# from PIL import Image
import requests
import pdb


os.environ["OPENAI_API_KEY"] = "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"
def gen_text(input_msg):

    prompt = "Write a stunning and attractive paragraph for powerpoint slides based on the keywords below: \n\n" + "\n\n" \
               + input_msg + "\n\n"
    openai.api_key = os.environ["OPENAI_API_KEY"]

    output_texts = list()
    for _ in range(3):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        output_texts.append(response["choices"][0]["text"])

    return output_texts



def gen_img(input_msg):
    # PARAMS = {'address':location}


    url = f"https://lexica.art/api/v1/search?q={input_msg}"
    response = requests.get(url)
    # response = requests.get(url, params = PARAMS)

    data = response.json()
    img_lst = data['images']
    img_links = [img['src'] for img in img_lst]

    if not os.path.exists(f'./img_folder/{input_msg}'):
        os.makedirs(f'./img_folder/{input_msg}')
    for img_link in img_links:
        img_response = requests.get(img_link)
        with open(img_link, 'wb') as ff:
            ff.write(img_response.content)


    return data
#     {
#     "images": [
#         {
#             // The ID of the image
#             "id": "0482ee68-0368-4eca-8846-5930db866b33",
#             // URL for the image's gallery
#             "gallery": "https://lexica.art?q=0482ee68-0368-4eca-8846-5930db866b33",
#             // Link to this image
#             "src": "https://image.lexica.art/md/0482ee68-0368-4eca-8846-5930db866b33",
#             // Link to an compressed & optimized version of this image
#             "srcSmall": "https://image.lexica.art/sm/0482ee68-0368-4eca-8846-5930db866b33",
#             // The prompt used to generate this image
#             "prompt": "cute chubby blue fruits icons for mobile game ui ",
#             // Image dimensions
#             "width": 512,
#             "height": 512,
#             // Seed
#             "seed": "1413536227",
#             // Whether this image is a grid of multiple images
#             "grid": false,
#             // The model used to generate this image
#             "model": "stable-diffusion",
#             // Guidance scale
#             "guidance": 7,
#             // The ID for this image's prompt
#             "promptid": "d9868972-dad8-477d-8e5a-4a0ae1e9b72b"
#             // Whether this image is classified as NSFW
#             "nsfw": false,
#         },
#     ...
#     ]
# }


if __name__ == '__main__':
    msg = 'apple'
    data = gen_img(msg)
    pdb.set_trace()

    print("Test over!!")



