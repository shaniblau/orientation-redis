import os
from redis import Redis

redis = Redis(host='localhost', port=6379, decode_responses=True)


def load(files_names):
    for name in files_names:
        with open(f"dogs/{name}", 'r') as file:
            file_content = file.read()
            redis.set(name, file_content)
