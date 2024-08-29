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
    @wraps(method)
    def wrapper(*args, **kwargs):
        """ Wrapped function """
        if kwargs:
            kwargs['self'].increment(method.__qualname__)
        else:
            args[0].increment(method.__qualname__)
        return method(*args, **kwargs)
    return wrapper


class Cache():
    """ The cache class for monitoring some stored data """

    def __init__(self) -> None:
        """ Initialization process of this class instance """
        self._redis = redis.Redis()

    @count_calls
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
