"""
Wraps granular functions in redis_service, postgres_service for user domain entities
"""
from postgres_service import add_entity, delete_entity
from models import User

def add_user(user):
    """
    INSERT user entity into DB using ORM via postgres_service
    """
    add_entity(user)

def delete_user(user):
    """
    DELETE user entity from DB using ORM via postgres_service
    """
    delete_entity(user)
    