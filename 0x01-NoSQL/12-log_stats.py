#!/usr/bin/env python3
"""
    Here the module description of Exo 12
"""
from typing import List, Tuple
from pymongo import MongoClient


def get_total_document_count(my_collection):
    """ Count all  the documents present in the collection """
    nb = my_collection.count_documents({})
    return nb


def parse_number_methods(my_collection,
                         methods: List[str]
                         ) -> List[Tuple[str, int]]:
    """ Parse the number of documents for each methos """
    res = []
    for x in methods:
        nb = my_collection.count_documents({"method": x})
        res.append((x, nb))
    return res


def count_documents_with(my_collection, field: str, pattern: str) -> int:
    """ Count documents with particular search """
    res = my_collection.count_documents({field: pattern})
    return res


def display_as_in_exercise(collection):
    """ Display as the exercise requires """
    nb = get_total_document_count(collection)
    print("{} logs".format(nb))
    print("Methods")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    data = parse_number_methods(my_collection=collection, methods=methods)
    for x, y in data:
        print("\tmethod {}: {}".format(x, y))
    count = count_documents_with(my_collection=collection,
                                 field="path", pattern='/status')
    print("{} status check".format(count))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    display_as_in_exercise(collection=collection)
