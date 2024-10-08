from app.models import Annotation
from app.database import db_session, init_db
import json
from flask import request, render_template, Flask, abort, send_from_directory
from app.images import create_test_dataset, get_dataset_tif_file

app = Flask(__name__)

# Download test dataset and convert tiff to dzi
REMAKE_TEST_DATASET = False
if REMAKE_TEST_DATASET:
    create_test_dataset()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/test_img"

init_db()


@app.route("/image/dzi", methods=["GET"])
def get_image():
    """Get DZI format image path from url"""
    tif_path = request.args.get('tif')
    print(tif_path)
    dzi_file = get_dataset_tif_file(tif_path)
    if dzi_file is None:
        abort(404)
    else:
        # return str(dzi_file)
        return send_from_directory(app.config['UPLOAD_FOLDER'],
                                   f"{tif_path}_img.dzi")


@app.route("/image_view")
def image_view():
    """Render image view html"""
    return render_template("index.html")


@app.route("/get_annotations", methods=["POST", "GET"])
def get_annotations():
    """Get annotations from database and return as json for given image and user"""
    data = request.json[0]

    annotation_list = []
    annotations = Annotation.query.filter(
        Annotation.image_id == data['source'],
        Annotation.user_id == data['user'])

    for annotation in annotations:
        print(annotation.annotation)
        annotation_list.append(
            json.loads(annotation.annotation.replace("\'", "\"")))

    print(annotation_list)

    return json.dumps(annotation_list)


@app.route('/add_annotations', methods=['POST', 'GET'])
def add_annotations():
    """Add annotations to database for given image and user"""
    data = request.json
    already_in_db = []
    # TODO Check if annotation i
    added_annotation_count = 0

    for dt in data:
        if Annotation.query.filter(
                Annotation.annotation_id == dt['id']).first():
            continue
        if dt["id"] in already_in_db:
            continue

        already_in_db.append(dt['id'])

        new_add = Annotation(dt['user'], dt['target']['source'], dt['id'],
                             str(dt))
        db_session.add(new_add)
        added_annotation_count += 1
    db_session.commit()

    return 'Success. Added {} new annotations'.format(added_annotation_count)


@app.route('/remove_annotations', methods=['POST', 'GET'])
def remove_annotations():
    """Remove annotations from database for given image and user"""
    data = request.json
    print(data)
    for dt in data:
        Annotation.query.filter(Annotation.annotation_id == dt['id'],
                                Annotation.user_id == dt['user'],
                                Annotation.image_id == dt['source']).delete()

    db_session.commit()

    return "success"


@app.route('/update_annotations', methods=['POST', 'GET'])
def update_annotations():
    """Update annotations in database for given image and user"""
    data = request.json
    for dt in data:
        annotation = Annotation.query.filter(
            Annotation.annotation_id == dt['id'],
            Annotation.user_id == dt['user'],
            Annotation.image_id == dt['source']).first()
        annotation.annotation = str(dt)

    db_session.commit()

    return "success"


# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
