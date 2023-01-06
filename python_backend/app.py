import json
from flask import Flask
from flask_cors import CORS

from ai.generator.img import RecommendationBasedImageGenerator, FreestyleImageGenerator
from ai.generator.text import AdPosterTextGenerator, FreestyleTextGenerator


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
    res = AdPosterTextGenerator.generate_text(content)
    return res


@app.route('/generate_ads_image/<content>', methods=['GET', 'POST'])
def generate_ads_image(content):
    res = RecommendationBasedImageGenerator.generate_img(content, top_k=1)
    return res


@app.route('/freely_generate_image/<content>', methods=['GET', 'POST'])
def freely_generate_image(content):
    res = FreestyleImageGenerator.generate_img(content, top_k=1)
    return res


@app.route('/freely_generate_text/<content>', methods=['GET', 'POST'])
def freely_generate_text(content):
    res = FreestyleTextGenerator.generate_text(content)
    return res



app.run()