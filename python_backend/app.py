import json
from flask import Flask
# from aimodel import real_get_image
from flask_cors import CORS

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


app.run()