from flask import Flask, request
from database import MongoDB_Handler as DB_Handler
import utils

app = Flask(__name__)
collection_filter = {
    "_id":0,
    "description":0,
    "url":0
} # filters the keys returned by database find

@app.route('/')
def get_all():
    category = request.args.get('category')
    query = {"category":category} if category else {}
    docs = db['exported_db_zara'].find(query, collection_filter)

    return utils.to_json(docs)

@app.route('/<id>')
def get_id(id):
    # TODO: get by id
    return

@app.route('/search')
def search():
    keywords = request.args.get('keywords')
    # TODO: implement
    # docs = findbykeywords(keywords)
    docs = None
    return utils.to_json(docs)


if __name__ == '__main__':
    with DB_Handler() as db:
        app.run()
