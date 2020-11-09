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
    """
    Node class used by flask-sqlalchemy ORM to generate DB migrations
    This class is used for validation using marshmallow-sqlalchemy
    """
    __tablename__ = 'Node'

    id = pdb.Column(pdb.Integer, primary_key=True)
    name = pdb.Column(pdb.String(25), nullable=False, unique=True)
    description = pdb.Column(pdb.String(100))
    nodeSettingsID = pdb.Column(pdb.Integer, pdb.ForeignKey('NodeSettings.id'))
    nodeSettings = pdb.relationship('NodeSettings', backref=pdb.backref('Node', uselist=False))
    location = pdb.Column(pdb.String(80))

    def __repr__(self):
        return '<Name: {}>'.format(self.name)

    def VERB(self):
        return {
            'nodeID': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location
        }

    def DTO(self):
        return {
            'nodeID': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location
        }

class NodeSettings(pdb.Model):
    """
    NodeSettings class used by flask-sqlalchemy ORM to generate DB migrations
    This class is used for validation using marshmallow-sqlalchemy
    """
    __tablename__ = 'NodeSettings'
 
    id = pdb.Column(pdb.Integer, primary_key=True)
    resolution = pdb.Column(pdb.String(15))
    ip = pdb.Column(pdb.String(15), nullable=False, unique=True)
    fps = pdb.Column(pdb.Integer)
    confidence = pdb.Column(pdb.Integer)

    def VERB(self):
        return {
            'resolution': {
                'pixelsX':self.pixelsX,
                'pixelsY':self.pixelsY
                },
            'ip': self.ip,
            'fps': self.fps, 
            'confidence': self.confidence
        }