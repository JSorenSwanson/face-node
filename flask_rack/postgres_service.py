"""
PSQL funcs wrapped by flask-SQLAlchemy
funcs leveraged by other application services [user_service, node_service, ...]
"""
from node_api import pdb
from flask import jsonify

def merge_entity(e):
    """
    Create or Merge enttiy using SQLAlchemy instance
    """
    pdb.session.merge(e)
    pdb.session.commit()

def add_entity(e):
    """
    Create entity (generic) using SQLAlchemy instance
    """
    pdb.session.add(e)
    pdb.session.commit()
   

def delete_entity(e):
    """
    Delete entity (generic) using SQLAlchemy instance
    """
    pdb.session.delete(e)
    pdb.session.commit()

def get_entity_by_id(cls, id_pk):
    """
    Return generic entity by PK
    """
    entity = cls.query.get(id_pk)
    return entity

def get_all_entities(cls):
    """
    Generic return all entities of class cls
    """
    return cls.query.all()