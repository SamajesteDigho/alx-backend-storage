#!/usr/bin/env python3
"""
    Here the underlying module of the web page analyser
"""
from functools import wraps
from typing import Callable
import redis
import requests


def cache_url(method: Callable) -> Callable:
    """ Here we get a decoration """
    red = redis.Redis()

    @wraps(method)
    def wrapper(*args, **kwargs) -> str:
        """ Here the wrapper """
        name = "count:{}".format(args[0])
        value = red.get(name)
        if value is None:
            value = 1
        else:
            value = int(value) + 1
        red.set(name=name, value=value)
        red.expire(name=name, time=10)
        return method(*args, **kwargs)
    return wrapper


@cache_url
def get_page(url: str) -> str:
    """ Let's define the function """
    return requests.get(url=url)
