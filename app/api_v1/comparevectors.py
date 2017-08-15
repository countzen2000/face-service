from flask import request, jsonify, make_response
from . import api
from ..science.compare_2_vectors import compare_2_vectors
import numpy as np

@api.route('/comparevectors', methods=['POST'])
def create_comparevectors():
    try:
        v1 = np.array(request.files['v1'])
        v2 = np.array(request.files['v2'])
    except:
        v1 = np.array(request.json['v1'])
        v2 = np.array(request.json['v2'])

    tolerance = compare_2_vectors(v1, v2)
    percentage = 1 - tolerance
    return make_response("Match percentage: {0}%".format(percentage*100), 200)
