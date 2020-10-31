"""
Collection of marshmallow-sqlalchemy schema classes
auto-generated from SQLAlchemy models (using PSQL session pdb)
OR strictly defined
"""
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import User
class UserSchema(SQLAlchemyAutoSchema):
    """
    Create User schema via SQLAlchemyAutoSchema
    """
    class Meta:
        """
        Create meta definitions for SQLAlchemy schema generation
        """
        model = User
        include_relationships = True
        load_instance = True
class LoginSchema(SQLAlchemyAutoSchema):
    """
    Create Login schema via SQLAlchemyAutoSchema
    Exclude unnecessary fields
    """
    class Meta: 
        """
        Create meta definitions for SQLAlchemy schema generation
        """ 
        model = User 
        include_relationships = True 
        exclude = ("username",)
