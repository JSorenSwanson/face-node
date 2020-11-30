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

def get_event_log(node):
    """
    Returns event logs associated with node from Redis
    """
    key_face = "F"+str(node)
    key_mask = "M"+str(node)

    return (tsdb_.get(key_face), tsdb_.get(key_mask))

def get_log_range(node, a, b):
    """
    Returns event logs associated with node from Redis as a range of entries
    between start of period (a) and end of period (b)
    """
    key_face = "F"+str(node)
    key_mask = "M"+str(node)
    range_face = tsdb_.range(key_face, a, b)
    range_mask = tsdb_.range(key_mask, a, b)
    (faces_x, faces_y) = zip(*range_face)
    (masks_x, masks_y) = zip(*range_mask)
    return (faces_x,faces_y,masks_x, masks_y)

def get_log_aggregate(node, a, b, agg_type='sum', bucket_size=60000):
    """
    Returns event logs associated with node from Redis as an aggregate across either type 'sum' (default) or 'avg'
    as a range of entries between start of period (a) and end of period (b)
    """
    key_face = "F"+str(node)
    key_mask = "M"+str(node)
    range_face = tsdb_.range(key_face, a, b, aggregation_type=agg_type, bucket_size_msec=bucket_size) 
    range_mask = tsdb_.range(key_mask, a, b, aggregation_type=agg_type, bucket_size_msec=bucket_size) 
    (faces_x, faces_y) = zip(*range_face)
    (masks_x, masks_y) = zip(*range_mask)
    return (faces_x,faces_y,masks_x, masks_y)