from flask import Flask, request
from database import MongoDB_Handler as DB_Handler
import utils

app = Flask(__name__)
filter = {
    "_id":0
} # filters the keys returned by database find

@app.route('/')
def get_all_url():
    category = request.args.get('category')
    query = {"category":category} if category else {}
    docs = db['exported_db_zara'].find(query, filter)
    return utils.to_json(docs)

if __name__ == '__main__':
    with DB_Handler() as db:
        app.run()
