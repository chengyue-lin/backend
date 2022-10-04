from flask import Flask, request, jsonify, render_template
from google.cloud import datastore
from google.cloud import storage

app = Flask(__name__)


@app.route("/analytics/dashboard")
def analytics():
    datastore_client = datastore.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')

    query = datastore_client.query(kind='Books')
    query_iter = query.fetch(start_cursor=None, limit=10)
    page = next(query_iter.pages)
    books = list(page)
    return render_template('homepage.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)

