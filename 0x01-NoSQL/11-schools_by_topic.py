#!/usr/bin/env python3
"""
    Here the module description of Exo 11
"""


def schools_by_topic(mongo_collection, topic):
    """ Schools offering a specific course """
    res = mongo_collection.find({"topics": topic})
    return res
