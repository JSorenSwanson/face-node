"""
### https://redis-py.readthedocs.io/en/stable/
 Creates a redis instance along our redis service host.
 Our redis service in docker-compose is listed as a dependency for this flask instance,
 which ensures 'redis' hostserver is instantiated.
"""
import redis 
import rejson import Client, Path
import time 

# you'll notice our redis container is named 'redis' and is exposed along port 6379 in our docker-compose.yml manifest.
cache_ = redis.Redis(host='redis', port=6379)
retry_ms = 1000 # total retry time (in milliseconds)

