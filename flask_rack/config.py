import os

# Get some variables from the OS environment table
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']

class Config(object):
    # Define Flask configurations
    CORS_HEADERS = 'Content-Type'

    # Configurations for SQLAlchemy and PostgreSQL
    POSTGRES_DEFAULT_USER = 'postgres'
    POSTGRES_USER = user
    POSTGRES_PASSWORD = password
    POSTGRES_DB = database
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + '@postgres:5432/' + POSTGRES_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = True
