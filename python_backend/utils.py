

import time
import openai
import os
# from PIL import Image
import requests
import pdb
import pathlib
from googletrans import Translator
from config import DEBUG
import numpy as np
import random

translator = Translator()

os.environ["OPENAI_API_KEY"] = "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"
def call_openai_text(prompt_text, n_returns=1):
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


def gen_text(input_msg, n_returns=1):
    if DEBUG:
        output_texts = [f"DEBUG {input_msg} DEBUG", f"DEBUG {input_msg} DEBUG", f"DEBUG {input_msg} DEBUG"]
    else:
        prompt = "Write a stunning and attractive paragraph for advertisement poster based on the keywords below: \n\n" + "\n\n" \
            + input_msg + "\n\n"
        output_texts = call_openai_text(prompt)
    return output_texts


def ai_freestyle_text_generate(input_msg):
    if DEBUG:
        input_msg = f"DEBUG {input_msg} DEBUG"
    else:
        prompt = f"{input_msg}"
        input_msg = call_openai_text(prompt)[0]
    return input_msg


def ai_freestyle_image_generate(input_msg, n_returns=3):
    if DEBUG:
        url = "https://lexica.art?q=0482ee68-0368-4eca-8846-5930db866b33"
    else:
        url = gen_img(input_msg)
        # url = "https://lexica.art?q=0482ee68-0368-4eca-8846-5930db866b33"
    return url
    # return input_msg


def gen_img(input_msg, topk=1, debug=DEBUG):
    if debug:
        return {'images': [], 'urls': ['https://lexica-serve-encoded-images.sharif.workers.dev/md/003cc1f0-e52a-400f-808f-358183156495'], 'local_pathes': ['/Users/ouyangzhihao/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/UtoDian/Github/AIGC/python_backend/img_folder/apple/0.jpg']}
    # PARAMS = {'address':location}
    print('Sending request to lexica server')
    # Enforce the text become english to call the lexica API
    # input_msg = translator.translate(input_msg).text
    url = f"https://lexica.art/api/v1/search?q={input_msg}"
    print(url)
    # import ipdb; ipdb.set_trace()
    response = requests.get(url)
    # import urllib.request
    # response = urllib.request.urlopen(url)
    # response = response.read()
    print("Finish Call")

    # response = requests.get(url, params = PARAMS)
    return_dict = {
        'images': [],
        'urls': [],
        'local_pathes': []
    }

    data = response.json()
    
    img_lst = data['images']
    # import ipdb; ipdb.set_trace()
    # randomly pickup one
    img_lst = img_lst[:10]
    assert 10 >= topk
    random.shuffle(img_lst)
    img_lst =img_lst[:topk]
    

    img_links = [img['src'] for img in img_lst]

    img_folder = pathlib.Path(f'./img_folder/{input_msg}')
    img_folder.mkdir(exist_ok=True)

    # if not os.path.exists(f'./img_folder/{input_msg}'):
    #     os.makedirs(f'./img_folder/{input_msg}')
    for i, img_link in enumerate(img_links):
        print(f"img_link {i}:", img_link)
        # img_response = requests.get(img_link)
        img_path = img_folder / f'{i}.jpg'
        # with open(img_path, 'wb') as ff:
        #     ff.write(img_response.content)
        
        # Bug: We need to jsonfiy image data
        # return_dict['imagqes'].append(img_response.content)
        return_dict['urls'].append(img_link)
        return_dict['local_pathes'].append(str(img_path.absolute()))
    
    return return_dict
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
    import ipdb;
    ipdb.set_trace()
    text = gen_text(msg, n_returns=1)
    # pdb.set_trace()
    print("Test over!!")



