from flask import Flask, jsonify, request
from flask_cors import CORS
from src.run_grisa import run_grisa
from src import utils
import os


app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong!')


@app.route('/grisa/upload', methods=['POST'])
def grisa_upload():
    if request.files.get('file'):
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        abs_path = utils.save_file(file)
    elif request.json.get('url'):
        url = request.json.get('url')
        abs_path = utils.save_file_from_url(url)
    else :
        return jsonify({'error': 'No file or url provided'})
    
    similiar_img_json, source_img_json = run_grisa(abs_path)

    os.remove(abs_path)
    return jsonify({
        'similar_imgs': similiar_img_json,
        'source_imgs': source_img_json
    })



@app.route('/grisa/upload/url/<path:url>', methods=['POST', 'GET'])
def grisa_upload_url(url):
    abs_path = utils.save_file_from_url(url)
    similiar_img_json, source_img_json = run_grisa(abs_path)
    os.remove(abs_path)

    return jsonify({
        'similar_imgs': similiar_img_json,
        'source_imgs': source_img_json
    })


if __name__ == '__main__':
    app.run(debug=True)

