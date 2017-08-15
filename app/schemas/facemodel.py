from .. import ma
from ..models.facemodel import Facemodel


class FacemodelSchema(ma.ModelSchema):

    class Meta:
        model = Facemodel


facemodel_schema = FacemodelSchema()
facemodels_schema = FacemodelSchema(many=True)
