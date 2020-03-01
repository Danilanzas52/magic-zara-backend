from flask import jsonify
from database import MongoDB_Handler


# Produce JSON from mongo docs
def to_json(docs):
    list = [doc for doc in docs]
    return jsonify(list)


def find_by_keywords(db, keyword_string):
    #Todo: specify in readme that is mandatory to create a text index in mongodb
    return db["zara"].find(
        {
            '$text': {
                '$search': keyword_string,
            }
        })
