from flask import Flask, request
from database import MongoDB_Handler as DB_Handler
from bson.objectid import ObjectId
import utils

app = Flask(__name__)
collection_filter = {
    "_id":0,
    "description":0,
    "url":0
} # filters the keys returned by database find

filter = {
    "_id": 0
}

@app.route('/')
def get_all():
    category = request.args.get('category')
    query = {"category":category} if category else {}
    docs = db['zara'].find(query, collection_filter)
    return utils.to_json(docs)

@app.route('/<id>')
def get_id(id):
    docs = db['zara'].find({"_id": ObjectId(id)}, filter)
    return utils.to_json(docs)

@app.route('/search')
def search():
    keywords = request.args.get('keywords')
    if keywords == None: return
    print(keywords)
    docs = utils.find_by_keywords(db, keywords)
    return utils.to_json(docs)


if __name__ == '__main__':
    with DB_Handler() as db:
        app.run()
