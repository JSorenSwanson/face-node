"""
Wraps granular functions in redis_service, postgres_service for node domain entities
"""
import json
import sqlalchemy
from flask import jsonify
from postgres_service import add_entity, delete_entity, get_entity_by_id, get_all_entities
from models import NodeObject, NodeSettings, pdb
from schemas import NodeSchema, NodeSettingsSchema
from marshmallow import ValidationError

node_schema = NodeSchema()
settings_schema = NodeSettingsSchema()

def create_node_settings(settings):
    """
    * Validates input `settings` against NodeObject schema generated via Marshmallow-SQLAlchemy
    * Generates  Node entity and commits to session iff schema is validated.
    """

    if not settings:
        return {"message":"Payload cannot be NULL"}, 400
    elif not settings["nodeAttributes"]:
        return {"message":"Node attributes cannot be NULL"}, 400
    elif not settings["nodeSettings"]:
        return {"message":"Node settings cannot be NULL"}, 400
    try:
        node_data = node_schema.load(settings["nodeAttributes"], session=pdb)
        settings_data = settings_schema.load(settings["nodeSettings"], session=pdb)
        node_data.nodeSettings = settings_data
    except ValidationError as ex:
        return ex.messages, 422
    try:
        add_entity(node_data)

    except sqlalchemy.exc.IntegrityError as ex:
        return 'Node Name or IP Address already exists.', 409

    return node_data.VERB()

def get_node_endpoints():
    """
    Retrieve representation of node endpoints as JSON serialized list 
    """
    entities = get_all_entities(NodeObject)
    return jsonify([NodeObject.DTOF(e, e.nodeSettings) for e in entities])
def get_nodes():
    """
    Retrieves all Node entries as JSON serialized list
    """
    entities = get_all_entities(NodeObject)
    return jsonify([NodeObject.DTO(e) for e in entities])

def get_node(node_id):
    """
    Retrieves JSON (VERBOSE) of Node entry by node_id
    """
    return get_entity_by_id(NodeObject,node_id).VERB()

def get_node_settings(node_id):
    """
    Retrieves JSON (VERBOSE) of Node settings entry associated with particular node_id
    """
    return get_entity_by_id(NodeObject,node_id).nodeSettings.VERB()