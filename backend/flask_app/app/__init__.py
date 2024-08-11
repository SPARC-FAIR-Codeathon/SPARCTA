# from app import app
from flask import send_file, request, render_template, Flask
from PIL import Image
import json
from tifffile import imread

from app.models import Image, Annotation

app = Flask(__name__)


@app.route('/')
def get_image():
    img = imread(
        '/home/devil/Documents/AnmolKiran/SPARC/2024-team-6/backend/flask_app/app/app/test.tif'
    )
    Image.fromarray(img).save('test.png')
    return send_file('test.png')


@app.route('/image_view')
def image_view():
    return render_template('index.html')


@app.route('/get_annotations', methods=['POST', 'GET'])
def get_annotations():
    data = request.form.to_dict()
    imageid = data['imageid']
    annotations = Image.filter(Image.image_name == imageid).first().annotations
    annotation_list = []

    for annotation in annotations:
        annotation_list.append({
            'annotation':
            annotation.annotation,
            'annotation_coordinates':
            annotation.annotation_coordinates
        })

    return json.dumps(annotation_list)


@app.route('/add_annotations', methods=['POST'])
def add_annotations():
    data = request.form.to_dict()
    annotations = data['annotations']
    imageid = data['imageid']
    images = Image.filter(Image.image_name == imageid).all()
    if not images:
        return 'image not found'
    elif len(images) > 1:
        return 'multiple images found'

    imges = images[0]

    for annotation in annotations:
        ann = Annotation(annotation['annotation'],
                         annotation['annotation_coordinates'])
        imges['annotations'].append(ann)
    db_session.commit()

    return 'success'


@app.route('/remove_annotations', methods=['POST'])
def remove_annotations():
    data = request.form.to_dict()
    for annotation in data['annotations']:
        Annotation.filter(Annotation.annotation == annotation).delete()

    db_session.commit()

    return 'success'


@app.route('/update_annotations', methods=['POST'])
def update_annotations():
    data = request.form.to_dict()

    for annotation in data['annotations']:
        ann = Annotation.filter(
            Annotation.annotation == annotation['annotation'])
        ann.update(
            {'annotation_coordinates': annotation['annotation_coordinates']})
    db_session.commit()

    return 'success'


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
