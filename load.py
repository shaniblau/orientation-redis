import os
from redis import Redis

redis = Redis(host='localhost', port=6379, decode_responses=True)


def load(path, files_names):
    for name in files_names:
        img = open(f"{path}/{name}", "rb").read()
        redis.set(name, img)

