#!/usr/bin/env python3
"""
    Here the module descrpition of the exercise
"""
from functools import wraps
from typing import Callable, Union
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """ Count number of times called """
    name = method.__qualname__
    @wraps(method)
    def wrapper(*args, **kwargs) -> str:
        """ Wrapped function """
        if kwargs:
            self = kwargs['self']
        else:
            self = args[0]
        self.increment(key=name)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Call hisotory decorator """
    @wraps(method)
    def wrapper(*args, **kwargs) -> str:
        """ The wrapper function """
        in_name = "{}:inputs".format(method.__qualname__)
        ot_name = "{}:outputs".format(method.__qualname__)
        if kwargs:
            self = kwargs['self']
            data = kwargs['data']
        else:
            self = args[0]
            data = args[1]

        self._redis.rpush(in_name, data)
        key = method(*args, **kwargs)
        self._redis.rpush(ot_name, key)
        return key
    return wrapper


class Cache():
    """ The cache class for monitoring some stored data """

    def __init__(self) -> None:
        """ Initialization process of this class instance """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store methode procedure and descriptions """
        key: str = str(uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self,
            key: str,
            fn: Union[Callable, None] = None
            ) -> Union[str, bytes, int, float]:
        """ Lets define the get method procedure """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_int(self, key: str) -> int:
        """ Get integer value from redis """
        return self.get(key=key, fn=int)

    def get_str(self, key: str) -> str:
        """ Get integer value from redis """
        return self.get(key=key, fn=str)

    def increment(self, key: str) -> int:
        """ Increment value stored """
        self._redis.incr(name=key, amount=1)

    def replay(self):
        """ Let's replay back the game """
        in_data = self._redis.lrange("Cache.store:inputs", start=0, end=-1)
        ot_data = self._redis.lrange("Cache.store:outputs", start=0, end=-1)

        print("Cache.store was called {} times:".format(len(in_data)))
        for x, y in zip(in_data, ot_data):
            d_x = x.decode("utf-8")
            d_y = y.decode("utf-8")
            print("Cache.store(*('{}',)) -> {}".format(d_x, d_y))
