from app import app
from flask import send_file
from PIL import Image
from tifffile import imread

@app.route('/')
def get_image():
    img = imread('./app/test.tif')
    Image.fromarray(img).save('./app/test.png')
    return send_file('./test.png')