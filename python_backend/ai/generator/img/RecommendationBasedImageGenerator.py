from ai.generator.img.ImageGenerator import ImageGenerator
import requests
import pathlib
import random

DEBUG = False

class RecommendationBasedImageGenerator(ImageGenerator):

    @classmethod
    def generate_img(cls, prompt, top_k=1):
        if DEBUG:
            return {'images': [], 'urls': [
                'https://lexica-serve-encoded-images.sharif.workers.dev/md/003cc1f0-e52a-400f-808f-358183156495'],
                    'local_pathes': [
                        '/Users/ouyangzhihao/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/UtoDian/Github/AIGC/python_backend/img_folder/apple/0.jpg']}
        # PARAMS = {'address':location}
        print('Sending request to lexica server')
        # Enforce the text become english to call the lexica API
        # prompt = translator.translate(prompt).text
        url = f"https://lexica.art/api/v1/search?q={prompt}"
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
        assert 10 >= top_k
        random.shuffle(img_lst)
        img_lst = img_lst[:top_k]

        img_links = [img['src'] for img in img_lst]

        ################### using pexel block #########################

        headers = {'Authorization': '563492ad6f917000010000013fcefd17749547ad943acd8de743dbf6'}
        url = f"https://api.pexels.com/v1/search?query={prompt}&per_page={top_k}"

        print(url)
        response = requests.get(url, headers=headers)

        data = response.json()

        img_lst = data['photos']

        assert len(img_lst) == top_k
        random.shuffle(img_lst)

        img_links = img_links + [img['src']['original'] for img in img_lst]
        print("Finish pexel call")

        ################### using unsplash block ######################
        # you need to register pexel to get authorization token or communicate with the team to unlock limit rate
        # current 50 queries per hour
        headers = {'Authorization': 'Client-ID IbtfMBjYynoAqCA0ISwJ45X1B4UhTbHTNm5lrT1EmAc'}
        url = f"https://api.unsplash.com/search/photos?per_page={top_k}&query={prompt}"

        print(url)
        response = requests.get(url, headers=headers)

        data = response.json()

        img_lst = data['results']

        assert len(img_lst) == top_k
        random.shuffle(img_lst)

        img_links = img_links + [img['urls']['raw'] for img in img_lst]

        print("Finish unsplash Call")

        img_folder = pathlib.Path(f'./img_folder/{prompt}')
        img_folder.mkdir(parents=True, exist_ok=True)

        # if not os.path.exists(f'./img_folder/{prompt}'):
        #     os.makedirs(f'./img_folder/{prompt}')
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