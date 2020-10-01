# Our cache-server (redis) service (lightweight keystore) (redis-services.py)
from .redis_service import *
import json 

def increment_node(node_id):
    return increment_key(node_id)

# Naíve SET, assumes we've performed validation on input. 
# Primary key for this object should be distinct; node_id is arbitrary. 
def create_node_settings(nodeid,settings):
    set_keyval(nodeid,json.dumps(settings))

# Naíve SET, assumes we've performed validation on input. 
def get_node_settings(node_id):
    return get_keyval(node_id)