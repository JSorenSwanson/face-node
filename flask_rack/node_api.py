"""
```flask``` service ingress.
node_api.py serves as a lightweight py httpserver
"""
import time
import jwt
import json
import logging
from functools import wraps
from datetime import datetime, timedelta
from models import NodeObject, NodeSettings, User, pdb
from flask import Flask, Blueprint, current_app, jsonify, request, abort

# Import Marshmallow schemas, functs
from schemas import UserSchema, LoginSchema
from marshmallow import ValidationError

# Import functions from service wrappers
from node_service import create_node_settings, get_node_settings, get_node, get_nodes
from user_service import add_user

# Support CORS on endpoints
from flask_cors import CORS

# Flask, cors instances
_flask = Flask(__name__)
CORS(_flask)
_flask.config.from_object("config.Config")

# Initialize database instance (PostgreSQL)
_flask.app_context().push()
pdb.init_app(_flask)
pdb.create_all()

# Generate Marshmallow Schema objects for validation
user_schema = UserSchema()
login_schema = LoginSchema() 

###############################################################################################
### Flask API endpoint definitions – Expect request payloads to be JSON serialized for brevity.
###############################################################################################

### DECORATORS
def auth_required(_fn):
    """
    Creates a decorator definition meant to wrap requests with authorization fn (`authorize`)
    Reads request body and then decodes jwt token (if present) and determines user's existence.
    `@auth_required` annotation can be used precedent to endpoint def'n to provide this functionality.
    """
    @wraps(_fn)
    def authorize(*args, **kwargs):
        headers = request.headers.get('Authorization', '').split()

        msg_expired = {
            'message': 'Token has expired, please login again to access this resource.',
            'authenticated': False
        }
        msg_error = {
            'message': 'Please login or register to access this resource.',
            'authenticated': False
        }
        if len(headers) < 2:
            return jsonify(msg_error), 401
          
        try:
            jwt_token = headers[1]
            jwtd = jwt.decode(jwt_token, current_app.config['SECRET_KEY'])
            #DEBUG TOKEN DECODE
            logging.warning('Protected request against token{\n[[%s]]\n(d)[%s]\nSUB=[%s]}', jwt_token, jwtd, jwtd['sub'])
            user_result = User.query.filter_by(email= jwtd['sub']).first()
            if not user_result:
                raise RuntimeError('No user found with email address: ' + jwtd['sub'])
            return _fn(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            logging.warning('Expired token in request!')
            return jsonify(msg_expired), 401
        except (jwt.InvalidTokenError, Exception) as ex:
            logging.warning('Invalid token in request – %s',ex)
            return jsonify(msg_error), 401
    return authorize

### ENDPOINTS
@_flask.route('/api/user/', methods=['POST'])
def register_user():
    """
    Inserts a user into psql db via flask-sqlalchemy ORM
    """
    payload = request.get_json()
    if not payload:
        return {"message":"No input data provided."}, 400
    try:
        user_data = user_schema.load(payload, session=pdb)
    except ValidationError as ex:
        return ex.messages, 422
        
    add_user(user_data)
    return jsonify(user_data.email_map()), 201

@_flask.route('/api/user/login', methods=['POST'])
def validate_user():
    """
    Attempts to validate payload against data retrieved from psql instance via ORM
    If valid, return JWT token
    """
    payload = request.get_json()
    if not payload:
        return {"message":"No input data provided."}, 400
    try:
        login_schema.load(payload, session=pdb)
    except ValidationError as ex:
        return ex.messages, 422

    uvalid = User.auth(**payload)
    if not uvalid:
        return jsonify({ 'message': 'Bad username and/or password.'}), 401
    jwt_token = jwt.encode({
        'sub': uvalid.email,
        'exp': datetime.utcnow() + timedelta(minutes=60),
        'iat': datetime.utcnow()},
        current_app.config['SECRET_KEY']
        )
    return jsonify({
        'token': jwt_token.decode('UTF-8')
        })


@_flask.route('/api/node/', methods=['POST'])
#@auth_required
def create_node():
    """
    Create node settings entity along nodeID
    """
    payload = request.get_json()
    return create_node_settings(payload)

@_flask.route('/api/nodesettings/<node_id>', methods=['GET'])
#@auth_required
def get_settings(node_id):
    """
    Return node settings along given node_id (PK)
    """
    val = get_node_settings(node_id)
    return val

@_flask.route('/api/node/', methods=['GET'])
def get_all_nodes():
    """
    Retrieve a JSON-serialized list of Node entities from postgres service using ORM framework
    """
    return get_nodes()


@_flask.route('/api/node/<node_id>')
def get_node_byid(node_id):
    """
    Retrieve JSON-serialized representation of Node entity from postgres service along node_id (PK)
    """
    return get_node(node_id)