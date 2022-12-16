import json
from flask import Flask
# from aimodel import real_get_image
from flask_cors import CORS
from utils import gen_text, gen_img
from flask import jsonify

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return json.dumps({'name': 'alice',
                       'email': 'alice@outlook.com'})

@app.route('/create_figma_file/<file_name>', methods=['GET', 'POST'])
def create_figma_file(file_name):
    return f'Create {file_name}\'s succeed!'


@app.route('/modify_title/<content>', methods=['GET', 'POST'])
def modify_title(content):
    return f'{content}'


@app.route('/generate_ads_text/<content>', methods=['GET', 'POST'])
def generate_ads_text(content):
    res = gen_text(content)
    res = res[0]
    return res


@app.route('/generate_ads_image/<content>', methods=['GET', 'POST'])
def generate_ads_image(content):
    res = gen_img(content)
    # res = jsonify(res)
    return res
    # with open("img.png", "rb") as image:
    #     f = image.read()
    #     b = bytearray(f)
    #     return b
    # res = res[0]
    # return res



app.run()