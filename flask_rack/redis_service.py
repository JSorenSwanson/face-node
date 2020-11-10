"""
 Service utilized as application service to interact with Redis DB via redis-py CLI wrapper;
 Redis host service initialized as parallel dependency to this service using docker-compose.
 ```redis``` service includes Redis distributed implementation of RedisTimeSeries DB. The client we use wraps
 RedisTimeSeries CLI commands by extending the redis-py interface – https://github.com/RedisTimeSeries/
"""

import time
# Python wrapper for RedisTimeSeries CLI, uses redistimeseries-py interface
from redistimeseries.client import Client

#  You'll notice our redis container is named 'redis'
#   and is exposed along port 6379 in our docker-compose.yml manifest.
tsdb_ = Client(host='redis', port=6379)

def generate_series(node):
    """
    Generates 2 timeseries keys (linkedlist heads) w/ Key=node{mask|face}
    """
    
    key_face = node+"Face"
    key_mask = node+"Mask"

    tsdb_.create(key_face, labels={'Time':'Faces'})
    tsdb_.create(key_mask, labels={'Time':'Masks'})

def log_event(faces, masks, node):
    """
    Generates events in series for Mask & Face TimeSeries.
    Assumes Mask & Face TimeSeries have been generated.
    """
    timestamp = int(time.time())
    key_face = node+"Face"
    key_mask = node+"Mask"

    tsdb_.add(key_face, timestamp, faces)
    tsdb_.add(key_mask, timestamp, masks)

def get_event_log(node):
    """
    Returns event logs associated with node from Redis
    """
    key_face = node+"Face"
    key_mask = node+"Mask"

    return (tsdb_.get(key_face), tsdb_.get(key_mask))

def get_log_range(node, a, b):
    """
    Returns event logs associated with node from Redis as a range of entries
    between start of period (a) and end of period (b)
    """
    key_face = node+"Face"
    key_mask = node+"Mask"
    range_face = tsdb_.range(key_face, a, b)
    range_mask = tsdb_.range(key_mask, a, b)
    return (range_face, range_mask)

def get_log_aggregate(node, a, b, agg_type='sum', bucket_size=10):
    """
    Returns event logs associated with node from Redis as an aggregate across either type 'sum' (default) or 'avg'
    as a range of entries between start of period (a) and end of period (b)
    """
    key_face = node+"Face"
    key_mask = node+"Mask"
    range_face = tsdb_.range(key_face, a, b, aggregation_type=agg_type, bucket_size_msec=bucket_size) 
    range_mask = tsdb_.range(key_mask, a, b, aggregation_type=agg_type, bucket_size_msec=bucket_size) 
    return (range_face, range_mask)