"""
POSTGRES & SQLALCHEMY configuration
"""
import os

# Get some variables from the OS environment table
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']
secret = os.environ['SECRET_KEY']

class Config(object):
    """
    Application context base configuration (FLASK/PG)
    """
    # Define Flask configurations
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = secret
    # Configurations for SQLAlchemy and PostgreSQL
    POSTGRES_DEFAULT_USER = 'postgres'
    POSTGRES_USER = user
    POSTGRES_PASSWORD = password
    POSTGRES_DB = database
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + '@postgres:5432/' + POSTGRES_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = True
