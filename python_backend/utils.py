import os
# from PIL import Image
import requests
import pdb
import pathlib
from googletrans import Translator
from config import DEBUG
import random

from ai.utils.openai_utils import OpenaiUtils

translator = Translator()

def gen_text_json(input_msg, n_returns=1):
    # input: the user input message
    # output: a json contains {title, sub_title, main_body, item1,item2,item3, decoration_text, time, address}

    result = {'title':[],
            'sub_title':[],
            'main_body':[],
            'item1':[],
            'item2':[],
            'item3':[],
            'decoration_text':[],
            'time':"",
            'address':"" 
        }
    
    prompt = "Write a three-words tagline, a long-sentence sub-title, a long product description, three item key texts, and one paragraph of decoration text for \n\n" \
            + input_msg + "\n"
    output_texts = OpenaiUtils.call_openai_text(prompt)  # a list of string
    text_lst = output_texts[0].split('\n')
    for text in text_lst:
        if text.startswith('Tagline:'):  # the title information
            result['title'] = text.split(':')[1].strip()

        elif text.startswith('Sub-title:'): # the sub-title information
            result['sub_title'] = text.split(':')[1].strip()
        elif text.startswith('Product Description:'): # the main-boday information
            result['main_body'] = text.split(':')[1].strip()

        elif text.startswith('1. '):  #  item 1
            result['item1'] = text.split('.')[1].strip()
        elif text.startswith('2. '): #  item 2
            result['item2'] = text.split('.')[1].strip()
        elif text.startswith('3. '):  # item 3
            result['item3'] = text.split('.')[1].strip()

        elif text.startswith('Decoration Text:'):  # decoration text information
            result['decoration_text'] = text.split(':')[1].strip()

    return result







def ai_freestyle_text_generate(input_msg):
    if DEBUG:
        input_msg = f"DEBUG {input_msg} DEBUG"
    else:
        prompt = f"{input_msg}"
        input_msg = OpenaiUtils.call_openai_text(prompt)[0]
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



    ################### using pexel block #########################

    headers = {'Authorization': '563492ad6f917000010000013fcefd17749547ad943acd8de743dbf6'}
    url = f"https://api.pexels.com/v1/search?query={input_msg}&per_page={topk}"

    print(url)
    response = requests.get(url, headers=headers)

    data = response.json()
    
    img_lst = data['photos']

    assert len(img_lst) == topk
    random.shuffle(img_lst)

    img_links = img_links + [img['src']['original'] for img in img_lst]
    print("Finish pexel call")



    ################### using unsplash block ######################
    # you need to register pexel to get authorization token or communicate with the team to unlock limit rate
    # current 50 queries per hour
    headers = {'Authorization': 'Client-ID IbtfMBjYynoAqCA0ISwJ45X1B4UhTbHTNm5lrT1EmAc'}
    url = f"https://api.unsplash.com/search/photos?per_page={topk}&query={input_msg}"

    print(url)
    response = requests.get(url, headers=headers)


    data = response.json()
    
    img_lst = data['results']

    assert len(img_lst) == topk
    random.shuffle(img_lst)


    img_links = img_links + [img['urls']['raw'] for img in img_lst]  

    
    print("Finish unsplash Call")




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


def gen_img_pexels(input_msg, topk=1):
    print('Sending request to pexel server')


    # you need to register pexel to get authorization token or communicate with the team to unlock limit rate
    # current 200 queries per hour
    headers = {'Authorization': '563492ad6f917000010000013fcefd17749547ad943acd8de743dbf6'}
    url = f"https://api.pexels.com/v1/search?query={input_msg}&per_page={topk}"

    print(url)
    response = requests.get(url, headers=headers)




    return_dict = {
        'images': [],
        'urls': [],
        'local_pathes': []
    }

    data = response.json()
    
    img_lst = data['photos']

    assert len(img_lst) == topk
    random.shuffle(img_lst)

    

    img_links = [img['src']['original'] for img in img_lst]
    img_folder = pathlib.Path(f'./img_folder/{input_msg}')
    # img_folder.mkdir(exist_ok=True)
    if not os.path.exists(f'./img_folder/{input_msg}'):
        os.makedirs(f'./img_folder/{input_msg}')
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

    
def gen_img_unsplash(input_msg, topk=1):
    print('Sending request to unsplash server')


    # you need to register pexel to get authorization token or communicate with the team to unlock limit rate
    # current 50 queries per hour
    headers = {'Authorization': 'Client-ID IbtfMBjYynoAqCA0ISwJ45X1B4UhTbHTNm5lrT1EmAc'}
    url = f"https://api.unsplash.com/search/photos?per_page={topk}&query={input_msg}"

    print(url)
    response = requests.get(url, headers=headers)



    return_dict = {
        'images': [],
        'urls': [],
        'local_pathes': []
    }

    data = response.json()
    
    img_lst = data['results']

    assert len(img_lst) == topk
    random.shuffle(img_lst)

    

    img_links = [img['urls']['raw'] for img in img_lst]
    img_folder = pathlib.Path(f'./img_folder/{input_msg}')
    # img_folder.mkdir(exist_ok=True)
    if not os.path.exists(f'./img_folder/{input_msg}'):
        os.makedirs(f'./img_folder/{input_msg}')
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





if __name__ == '__main__':
    # msg = 'apple'
    # data = gen_img(msg)
    # import ipdb;
    # ipdb.set_trace()
    # text = gen_text(msg, n_returns=1)


    # msg = "Whatsmore cake party at 500 Lawrence Expy, Sunnyvale, CA 94085 this Saturday at 11:00 pm"
    # json_file = gen_text_json(msg)

    msg = 'nature'
    # results = gen_img_pexels(msg, 3)
    results = gen_img_unsplash(msg, 3)
    pdb.set_trace()
    print("Test over!!")



