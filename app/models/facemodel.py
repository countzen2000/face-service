from .. import db


class Facemodel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    # Additional fields

    def __repr__(self):
        return 'Facemodel {}>'.format(self.id)
