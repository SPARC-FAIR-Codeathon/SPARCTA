import json
from flask import request, render_template, Flask, abort, send_from_directory
from app.models import Image, Annotation
from app.images import create_test_dataset, get_dataset_tif_file

app = Flask(__name__)

# Download test dataset and convert tiff to dzi
REMAKE_TEST_DATASET = False
if REMAKE_TEST_DATASET:
    create_test_dataset()


@app.route("/image/dzi", methods=["GET"])
def get_image():
    tif_path = request.args.get('tif')
    dzi_file = get_dataset_tif_file(tif_path)
    if dzi_file is None:
        abort(404)
    else:
        return send_from_directory(dzi_file.parent, dzi_file.name)

@app.route("/image_view")
def image_view():
    return render_template("index.html")


@app.route("/get_annotations", methods=["POST", "GET"])
def get_annotations():
    data = request.json
    imageid = data['imageid']
    annotations = Image.filter(Image.image_name == imageid).first().annotations
    annotation_list = []

    for annotation in annotations:
        annotation_list.append(
            {
                "annotation": annotation.annotation,
                "annotation_coordinates": annotation.annotation_coordinates,
            }
        )

    return json.dumps(annotation_list)


@app.route('/add_annotations', methods=['POST', 'GET'])
def add_annotations():
    data = request.json
    print(data)
    imageid = data['image_id']
    images = Image.filter(Image.id == imageid).all()
    if not images:
        return "image not found"
    elif len(images) > 1:
        return 'multiple images found'
    annotations = data['annotations']

    imges = images[0]

    for annotation in annotations:
        ann = Annotation(annotation["annotation"], annotation["annotation_coordinates"])
        imges["annotations"].append(ann)
    db_session.commit()

    return "success"


@app.route('/remove_annotations', methods=['POST', 'GET'])
def remove_annotations():
    data = request.json
    for annotation in data['annotations']:
        Annotation.filter(Annotation.annotation == annotation).delete()

    db_session.commit()

    return "success"


@app.route('/update_annotations', methods=['POST', 'GET'])
def update_annotations():
    data = request.json

    for annotation in data["annotations"]:
        ann = Annotation.filter(Annotation.annotation == annotation["annotation"])
        ann.update({"annotation_coordinates": annotation["annotation_coordinates"]})
    db_session.commit()

    return "success"


# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
