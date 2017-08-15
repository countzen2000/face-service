from flask import jsonify, request, make_response
from io import BytesIO
from skimage import io
from . import api
from ..science.compare_2_images import compare_2_images


@api.route('/compareimages', methods=['POST'])
def compare_images():
    # try:
    target_file = request.files['target']
    match_file = request.files['match']

    in_memory_file = BytesIO()
    target_file.save(in_memory_file)
    target_image = io.imread(target_file)

    in_memory_file = BytesIO()
    match_file.save(in_memory_file)
    match_image = io.imread(match_file)

    marks = compare_2_images(target_image, match_image)
    rep = make_response(str(marks), 200)
    # except:
    #     rep = make_response("Image file went wrong.", 404)

    return rep
