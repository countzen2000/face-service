from flask import request, jsonify, make_response
from . import api
from io import BytesIO
from ..science.build_model import make_model
from skimage import io

@api.route('/facemodel', methods=['GET'])
def get_facemodel():
    return "herro"


@api.route('/facemodel', methods=['POST'])
def create_facemodel():

    try:
        file = request.files['file']

        in_memory_file = BytesIO()
        file.save(in_memory_file)
        img = io.imread(file)

        marks = make_model(img)
        rep = make_response(str(marks), 200)
    except:
        rep = make_response("Image file went wrong.", 404)

    return rep
