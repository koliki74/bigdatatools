"""
HASVITHA KOLIKINENI
ASSIGNMENT 3 SUBMISSION
BIG DATA TOOLS AND TECHNIQUES
"""
import redis
import json


# RedisHandler stores the JSON data into Redis by converting the json data into string.
class RedisHandler:

    def __init__(self, host="localhost", port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def insert_data(self, key, data):
        json_data = json.dumps(data)
        self.r.set(key, json_data)
