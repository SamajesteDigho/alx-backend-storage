#!/usr/bin/env python3
"""
    Here the module description of Exo 10
"""


def update_topics(mongo_collection, name, topics):
    """ Change topics based on the name """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
        upsert=False
    )