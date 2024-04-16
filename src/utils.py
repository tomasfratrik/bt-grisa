import requests
import uuid
import os

IMG_DIR = os.path.join(os.getcwd(), 'images')

def save_file_from_url(url):
    filename = f'{uuid.uuid4()}.jpg'
    img = requests.get(url)
    with open(os.path.join(IMG_DIR, filename), 'wb') as f:
        f.write(img.content)
    
    abs_path = os.path.join(IMG_DIR, filename)
    return abs_path

def save_file(file):
    filename = f'{uuid.uuid4()}.jpg'
    file.save(os.path.join(IMG_DIR, filename))
    abs_path = os.path.join(IMG_DIR, filename)
    return abs_path