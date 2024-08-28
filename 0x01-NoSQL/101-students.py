#!/usr/bin/env python3
"""
    Here the module for bonus question 101
"""


def top_students(mongo_collection):
    """ Get the top students by thier averages """
    scores = mongo_collection.aggregate([
        {"$project": {
            "_id": 1,
            "average": {"$avg": "$topics.score"}
        }}
    ])
    for x in scores:
        mongo_collection.update_one(
            {"_id": x['_id']},
            {"$set": {"averageScore": x["average"]}}
        )
    return mongo_collection.find()
