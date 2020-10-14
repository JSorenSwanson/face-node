### https://redis-py.readthedocs.io/en/stable/
# Creates a redis instance along our redis service host. 
# Our redis service in docker-compose is listed as a dependency for this flask instance, which ensures a 'redis' 
# hostserver is instantiated. 
import redis 
import time 

# you'll notice our redis container is named 'redis' and is exposed along port 6379 in our docker-compose.yml manifest.
_cache = redis.Redis(host='redis', port=6379)

# Generalized redis setter along key:val input, generally we're storing serialized JSON objs as values. 
#def setKey(key,value):

# Returns number of hits for a given node along arbitrary ID after incrementing value associated to input key by n.
def increment_key(key, n=1):
    # Retry limit for redis connection (ms)
    retry_ms = 150
    while True:
        try:
            return _cache.incr(key, n)
        except redis.exceptions.ConnectionError as exc:
            if retry_ms == 0:
                raise exc
            retry_ms -= 1
            time.sleep(1)

# SETS value of key in our redis cache
# Naíve SET, assumes we've performed validation on pairs. 
def set_keyval(key,val):
    # Retry limit for redis connection (ms)
    retry_ms = 1000
    while True:
        try:
            return _cache.set(key,val)
        except redis.exceptions.ConnectionError as exc:
            if retry_ms == 0:
                raise exc
            retry_ms -= 1
            time.sleep(1)

# SETS value of key in our redis cache
def get_keyval(key):
   
     # Retry limit for redis connection (ms)
    retry_ms = 1000
    while True:
        try:
            return _cache.get(key)
        except redis.exceptions.ConnectionError as exc:
            if retry_ms == 0:
                raise exc
            retry_ms -= 1
            time.sleep(1)