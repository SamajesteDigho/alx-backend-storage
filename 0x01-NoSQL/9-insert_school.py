#!/usr/bin/env python3
"""
    Here the module description of Exo 09
"""


def insert_school(mongo_collection, **kwargs):
    """ Insert a new document in a collection """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
