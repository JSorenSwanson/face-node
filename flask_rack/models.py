# Extension for Flask: Flask-SQLAlchemy
# Flask-SQLAlchemy lets us define database objects in models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User: {}>'.format(self.username)

class NodeObject(db.Model):

    __tablename__ = 'allNodes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    desc = db.Column(db.String(100))
    ip = db.Column(db.String(15))
    fps = db.Column(db.Integer)
    resID = db.Column(db.Integer, db.ForeignKey('res.id'))
    res = db.relationship('NodeCameraResolution', backref=db.backref('allNodes', uselist=False))
    activity = db.relationship('NodeActivityEntry', backref='allNodes')
    location = db.Column(db.String(80))

    def __repr__(self):
        return '<Name: {}>'.format(self.name)

    def export_all_data(self):
        return {
            'name': self.name,
            'desc': self.desc
        }

    def export_DTO(self):
        return {
            'name': self.name,
            'desc': self.desc
        }

class NodeCameraResolution(db.Model):

    __tablename__ = 'res'

    id = db.Column(db.Integer, primary_key=True)
    pixelsX = db.Column(db.Integer)
    pixelsY = db.Column(db.Integer)

    def __repr__(self):
        return '<pixelsX: {}, pixelsY: {}>'.format(self.pixelsX, self.pixelsY)

class NodeActivityEntry(db.Model):

    __tablename__ = 'activityEntries'

    id = db.Column(db.Integer, primary_key=True)
    counter = db.Column(db.Integer)
    parentNodeID = db.Column(db.Integer, db.ForeignKey('allNodes.id'))

    def __repr__(self):
        return '<Statistic: {}>'.format(self.counter)

class QuickQueries:
    def get_all(model):
        data = model.query.all()
        return data


    def add_instance(model, **kwargs):
        instance = model(**kwargs)
        db.session.add(instance)
        commit_changes()


    def delete_instance(model, id):
        model.query.filter_by(id=id).delete()
        commit_changes()


    def edit_instance(model, id, **kwargs):
        instance = model.query.filter_by(id=id).all()[0]
        for attr, new_value in kwargs.items():
            setattr(instance, attr, new_value)
        commit_changes()


    def commit_changes():
        db.session.commit()
