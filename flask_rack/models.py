"""
 Extension for Flask: Flask-SQLAlchemy
 Flask-SQLAlchemy lets us define database objects in models.py
"""
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
pdb = SQLAlchemy()

class User(pdb.Model):
    """
    User class used by flask-sqlalchemy ORM to generate DB migrations
    This class is used for validation using marshmallow-sqlalchemy
    """
    # Define name for table built from ORM migration
    __tablename__ = 'User'

    # Define table fields, types/restrictions
    uid = pdb.Column(pdb.Integer, primary_key=True)
    username = pdb.Column(pdb.String(25), nullable=False)
    email = pdb.Column(pdb.String(320), unique=True, nullable=False)
    password = pdb.Column(pdb.String(10000), nullable=False)
    # TODO – define relationships between Users and Nodes

    # Define initialization behavior for Users
    def __init__(self, email, password, username):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password, method='sha256')

    @classmethod
    def auth(cls, **kwargs):
        """
        Defines method for User which checks hashed password against associated email address
        """
        email = kwargs.get('email')
        password = kwargs.get('password')
    
        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def email_map(self):
        """
        Return map of UserID->UserEmail
        """
        return dict(id=self.uid, email=self.email)

class NodeObject(pdb.Model):

    __tablename__ = 'Node'

    id = pdb.Column(pdb.Integer, primary_key=True)
    name = pdb.Column(pdb.String(25))
    desc = pdb.Column(pdb.String(100))
    ip = pdb.Column(pdb.String(15))
    fps = pdb.Column(pdb.Integer)
    resID = pdb.Column(pdb.Integer, pdb.ForeignKey('res.id'))
    res = pdb.relationship('NodeCameraResolution', backref=pdb.backref('Node', uselist=False))
    activity = pdb.relationship('NodeActivityEntry', backref='Node')
    location = pdb.Column(pdb.String(80))

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

class NodeCameraResolution(pdb.Model):

    __tablename__ = 'res'

    id = pdb.Column(pdb.Integer, primary_key=True)
    pixelsX = pdb.Column(pdb.Integer)
    pixelsY = pdb.Column(pdb.Integer)

    def __repr__(self):
        return '<pixelsX: {}, pixelsY: {}>'.format(self.pixelsX, self.pixelsY)

class NodeActivityEntry(pdb.Model):

    __tablename__ = 'activityEntries'

    id = pdb.Column(pdb.Integer, primary_key=True)
    counter = pdb.Column(pdb.Integer)
    parentNodeID = pdb.Column(pdb.Integer, pdb.ForeignKey('Node.id'))

    def __repr__(self):
        return '<Statistic: {}>'.format(self.counter)

# Boilerplate pseducode reference 
"""class QuickQueries:
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
"""