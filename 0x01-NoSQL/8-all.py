#!/ussr/bin/env python3
"""
    Here the module description of Exo 08
"""


def list_all(mongo_collection):
    """ List all collections in a db """
    return mongo_collection.find({})