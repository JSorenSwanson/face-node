import time
import logging
from datetime import datetime

# Input schemas (Provided by Marshmallow framework) 
from schemas.node_schemas import *
# Node services which invoke granular Redis services
from services.node_service import *

# Construct schema object(s) for input validation 
# In next iteration, we will utilize marshmallow-flask-sqlalchemy to automate schema generation from our ORM definitions(!)
_node_settings_schema = NodeSettingsSchema()

# Flask and api doc
from flask import Flask, jsonify, request, abort
# Support CORS on endpoints
from flask_cors import *

# Flask, cors instances
_flask = Flask(__name__)
CORS(_flask)
_flask.config['CORS_HEADERS'] = 'Content-Type'
flaskID = 'NodeFlask'

logging.getLogger('flask_cors').level = logging.DEBUG


@_flask.route('/')
def hello_world(): 
    return 'Hello from inside our Docker container!'

### Flask API endpoint definitions – Expect request payloads to be JSON serialized for brevity. 
# Create node settings (to Redis cache) along nodeid:settings(JSON)
@_flask.route('/api/node/', methods=['POST'])
#@cross_origin() -- atomic cross_origin grants
def create_settings():
    payload = request.get_json()
    # validate our request payload against the schema we've created for the input-type.
    errors = _node_settings_schema.validate(payload)
    if errors:
        abort(400, str(errors))
    # now that we've validated our data fidelity we can begin using it in our service(node_service.py) functions. 
    create_node_settings(payload['node_id'], payload)
    return 'Successfully updated node settings.'

# Return node settings (from Redis cache) along nodeid:settings(JSON)
@_flask.route('/api/nodesettings/<node_id>', methods=['GET'])
def get_settings(node_id):
    val = get_node_settings(node_id)
    return val

@_flask.route('/api/node/', methods=['GET'])
def get_all_nodes():
    return 'retrieving all nodes...'

# Returns redis cache value associated with node ID in the form of a formatted string. 
# Eventually this endpoint will return more information related to our node object. Before we've our DB designed a cache will do for stack demonstrability. 
@_flask.route('/api/node/<node_id>')
def get_node_byid(node_id):
    # create a time for the event here, we'll eventually store in our redis keystore along our key. 
    eventTime = datetime.now().strftime("%H:%M:%S")
    # increments keystore val along node_id 
    ncount = increment_node(node_id)
    return 'Node <b><u>{}</u></b> has seen {} masks at {}.'.format(node_id, ncount, eventTime)