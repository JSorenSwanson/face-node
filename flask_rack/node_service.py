"""
Wraps granular functions in redis_service, postgres_service for node domain entities
"""
from redis_service import get_keyval, set_keyval, increment_key
import json

def increment_node(node_id):
    return increment_key(node_id)

def create_node_settings(nodeid,settings):
    """
    Naíve SET, assumes we've performed validation on input.
    Primary key for this object should be distinct; node_id is arbitrary.
    """
    set_keyval(nodeid,json.dumps(settings))

def get_node_settings(node_id):
    """
    Naíve GET, assumes we've performed validation on input.
    """
    return get_keyval(node_id)