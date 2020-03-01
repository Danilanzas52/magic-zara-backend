from flask import jsonify

# Produce JSON from mongo docs
def to_json(docs):
    list = [doc for doc in docs]
    return jsonify(list)
