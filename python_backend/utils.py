

import time
import openai
import os
# from PIL import Image
import requests
import pdb
import pathlib

os.environ["OPENAI_API_KEY"] = "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"
def gen_text(input_msg, n_returns=3):
    prompt = "Write a stunning and attractive paragraph for powerpoint slides based on the keywords below: \n\n" + "\n\n" \
               + input_msg + "\n\n"
    openai.api_key = os.environ["OPENAI_API_KEY"]

    output_texts = list()
    for _ in range(n_returns):
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


def gen_img(input_msg, topk=1, debug=False):
    if debug:
        return {'images': [], 'urls': ['https://lexica-serve-encoded-images.sharif.workers.dev/md/003cc1f0-e52a-400f-808f-358183156495'], 'local_pathes': ['/Users/ouyangzhihao/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/UtoDian/Github/AIGC/python_backend/img_folder/apple/0.jpg']}
    # import ipdb; ipdb.set_trace()
    # PARAMS = {'address':location}
    print('Sending request to lexica server')
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
    img_lst = data['images'][:topk]
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



