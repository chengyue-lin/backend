import os, json
from functools import wraps
import requests
from flask import Flask, request, jsonify, render_template, abort
from google.cloud import storage
from google.cloud import datastore

import logging

app = Flask(__name__)

CLOUD_STORAGE_BUCKET = "library-api"

@app.errorhandler(400)
def error_occur(e):
    logging.error("An error 400 occurs")
    return "An error occurs.", 400

@app.errorhandler(406)
def isbn_invalid(e):
    logging.error("isbn code is invalid")
    return "isbn code is invalid.", 406

@app.errorhandler(404)
def book_not_found(e):
    logging.error("Book not found")
    return "Book not found.", 404

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get("X-Api-Key") != "abcdef123456":
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/api/books", methods=['GET', 'POST'])
@require_api_key
def books():
    if request.method == 'GET':
        datastore_client = datastore.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        if request.args.get('author') is not None and request.args.get('language') is not None:

            query = datastore_client.query(kind='Books')
            query.add_filter("author", "=", request.args.get('author'))
            query.add_filter("language", "=", request.args.get('language'))
            if request.args.get('cursor') is None:
                cursor = None
            else:
                cursor = request.args.get('cursor')
            query_iter = query.fetch(start_cursor=cursor, limit=10)
            page = next(query_iter.pages)
            books = list(page)
            next_cursor = query_iter.next_page_token
            json_array = []
            for entity in books:
                dict = {}
                dict['isbn'] = str(entity['isbn'])
                dict['author'] = str(entity['author'])
                dict['image_public_url'] = entity['image_public_url']
                dict['language'] = str(entity['language'])
                dict['title'] = str(entity['title'])
                dict['page'] = int(entity['page'])
                dict['year'] = int(entity['year'])
                dict['cursor'] = next_cursor if next_cursor else None
                json_array.append(dict)

            return jsonify(json_array), 200

        elif request.args.get('author') is not None:
            query = datastore_client.query(kind='Books')
            query.add_filter("author", "=", request.args.get('author'))
            if request.args.get('cursor') is None:
                cursor = None
            else:
                cursor = request.args.get('cursor')
            query_iter = query.fetch(start_cursor=cursor, limit=10)
            page = next(query_iter.pages)
            books = list(page)
            next_cursor = query_iter.next_page_token
            json_array = []
            for entity in books:
                dict = {}
                dict['isbn'] = str(entity['isbn'])
                dict['author'] = str(entity['author'])
                dict['image_public_url'] = entity['image_public_url']
                dict['language'] = str(entity['language'])
                dict['title'] = str(entity['title'])
                dict['page'] = int(entity['page'])
                dict['year'] = int(entity['year'])
                dict['cursor'] = next_cursor if next_cursor else None
                json_array.append(dict)

            return jsonify(json_array), 200

        elif request.args.get('language') is not None:
            query = datastore_client.query(kind='Books')
            query.add_filter("language", "=", request.args.get('language'))
            if request.args.get('cursor') is None:
                cursor = None
            else:
                cursor = request.args.get('cursor')
            query_iter = query.fetch(start_cursor=cursor, limit=10)
            page = next(query_iter.pages)
            books = list(page)
            next_cursor = query_iter.next_page_token
            json_array = []
            for entity in books:
                dict = {}
                dict['isbn'] = str(entity['isbn'])
                dict['author'] = str(entity['author'])
                dict['image_public_url'] = entity['image_public_url']
                dict['language'] = str(entity['language'])
                dict['title'] = str(entity['title'])
                dict['page'] = int(entity['page'])
                dict['year'] = int(entity['year'])
                dict['cursor'] = next_cursor if next_cursor else None
                json_array.append(dict)

            return jsonify(json_array), 200

        elif request.args.get('flexible') is not None:
            query = datastore_client.query(kind='Books')
            text = request.args.get('flexible')
            all_infos = list(query.fetch())
            json_array = []
            for entity in all_infos:
                if text in str(entity['isbn']):
                    dict = {}
                    dict['isbn'] = str(entity['isbn'])
                    dict['author'] = str(entity['author'])
                    dict['image_public_url'] = entity['image_public_url']
                    dict['language'] = str(entity['language'])
                    dict['title'] = str(entity['title'])
                    dict['page'] = int(entity['page'])
                    dict['year'] = int(entity['year'])
                    json_array.append(dict)
                elif text in str(entity['language']):
                    dict = {}
                    dict['isbn'] = str(entity['isbn'])
                    dict['author'] = str(entity['author'])
                    dict['image_public_url'] = entity['image_public_url']
                    dict['language'] = str(entity['language'])
                    dict['title'] = str(entity['title'])
                    dict['page'] = int(entity['page'])
                    dict['year'] = int(entity['year'])
                    json_array.append(dict)
                elif text in str(entity['author']):
                    dict = {}
                    dict['isbn'] = str(entity['isbn'])
                    dict['author'] = str(entity['author'])
                    dict['image_public_url'] = entity['image_public_url']
                    dict['language'] = str(entity['language'])
                    dict['title'] = str(entity['title'])
                    dict['page'] = int(entity['page'])
                    dict['year'] = int(entity['year'])
                    json_array.append(dict)
                elif text in str(entity['title']):
                    dict = {}
                    dict['isbn'] = str(entity['isbn'])
                    dict['author'] = str(entity['author'])
                    dict['image_public_url'] = entity['image_public_url']
                    dict['language'] = str(entity['language'])
                    dict['title'] = str(entity['title'])
                    dict['page'] = int(entity['page'])
                    dict['year'] = int(entity['year'])
                    json_array.append(dict)
                elif text in str(entity['page']):
                    dict = {}
                    dict['isbn'] = str(entity['isbn'])
                    dict['author'] = str(entity['author'])
                    dict['image_public_url'] = entity['image_public_url']
                    dict['language'] = str(entity['language'])
                    dict['title'] = str(entity['title'])
                    dict['page'] = int(entity['page'])
                    dict['year'] = int(entity['year'])
                    json_array.append(dict)
                elif text in str(entity['year']):
                    dict = {}
                    dict['isbn'] = str(entity['isbn'])
                    dict['author'] = str(entity['author'])
                    dict['image_public_url'] = entity['image_public_url']
                    dict['language'] = str(entity['language'])
                    dict['title'] = str(entity['title'])
                    dict['page'] = int(entity['page'])
                    dict['year'] = int(entity['year'])
                    json_array.append(dict)
            return jsonify(json_array), 200

        else:
            query = datastore_client.query(kind='Books')
            if request.args.get('cursor') is None:
                cursor = None
            else:
                cursor = request.args.get('cursor')
            query_iter = query.fetch(start_cursor=cursor, limit=10)
            page = next(query_iter.pages)
            books = list(page)
            next_cursor = query_iter.next_page_token
            json_array = []
            for entity in books:
                dict = {}
                dict['isbn'] = str(entity['isbn'])
                dict['author'] = str(entity['author'])
                dict['image_public_url'] = entity['image_public_url']
                dict['language'] = str(entity['language'])
                dict['title'] = str(entity['title'])
                dict['page'] = int(entity['page'])
                dict['year'] = int(entity['year'])
                dict['cursor'] = next_cursor if next_cursor else None
                json_array.append(dict)

            return jsonify(json_array), 200

    if request.method == 'POST':
        string_json = request.form["data"]
        data = json.loads(string_json)
        photo = request.files['file']
        author = data['author']
        language = data['language']
        page = data['page']
        title = data['title']
        year = data['year']
        storage_client = storage.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        bucket_name = CLOUD_STORAGE_BUCKET
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(photo.filename)
        blob.upload_from_string(photo.read(), content_type=photo.content_type)
        datastore_client = datastore.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        kind = 'Books'
        key = datastore_client.key(kind)
        entity = datastore.Entity(key)
        entity['author'] = str(author) if author else "no provide"
        entity['language'] = str(language) if language else "no provide"
        entity['page'] = int(page) if page else 1
        entity['title'] = str(title) if title else "no provide"
        entity['year'] = int(year) if year else 2020
        entity['isbn'] = ""
        entity['image_public_url'] = blob.public_url
        datastore_client.put(entity)

        return "post a new book", 201



@app.route("/api/books/<isbn>", methods=['GET', 'POST', 'PUT', 'DELETE'])
@require_api_key
def operation(isbn):
    if request.method == 'GET':
        if not str(isbn).isdigit() or len(isbn) != 13:
            return "invalid isbn", 406
        datastore_client = datastore.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        query = datastore_client.query(kind='Books')
        book_entities = list(query.fetch())

        json_array = []
        dict1 = {}

        for entity in book_entities:
            if entity['isbn'] == isbn:
                dict1['isbn'] = str(entity['isbn'])
                dict1['author'] = str(entity['author'])
                dict1['image_public_url'] = entity['image_public_url']
                dict1['language'] = str(entity['language'])
                dict1['title'] = str(entity['title'])
                dict1['page'] = int(entity['page'])
                dict1['year'] = int(entity['year'])
                json_array.append(dict1)
        if dict1 is None:
            return "book not found", 404
        return jsonify(json_array), 200

    if request.method == 'POST':
        if not str(isbn).isdigit() or len(isbn) != 13:
            return "invalid isbn", 406

        string_json = request.form["data"]
        data = json.loads(string_json)
        photo = request.files['file']
        author = data['author']
        language = data['language']
        page = data['page']
        title = data['title']
        year = data['year']
        storage_client = storage.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        bucket_name = CLOUD_STORAGE_BUCKET
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(photo.filename)
        blob.upload_from_string(photo.read(), content_type=photo.content_type)
        print(f"File uploaded: {photo.filename} to {blob.public_url}")

        datastore_client = datastore.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        kind = 'Books'
        key = datastore_client.key(kind)
        entity = datastore.Entity(key)
        entity['author'] = str(author) if author else "no provide"
        entity['language'] = str(language) if language else "no provide"
        entity['page'] = int(page) if page else 1
        entity['title'] = str(title) if title else "no provide"
        entity['year'] = int(year) if year else 2020
        entity['isbn'] = str(isbn) if isbn else "0000000000000"
        entity['image_public_url'] = blob.public_url
        datastore_client.put(entity)

        return "post a new book", 201

    if request.method == 'PUT':
        if not str(isbn).isdigit() or len(isbn) != 13:
            return "invalid isbn", 406
        string_json = request.form["data"]
        data = json.loads(string_json)

        datastore_client = datastore.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        query = datastore_client.query(kind='Books')
        book_entities = list(query.fetch())
        json_array = []
        dict1 = {}
        for entity in book_entities:
            if entity['isbn'] == isbn:
                if "author" in data:
                    author = data['author']
                    entity['author'] = str(author)
                if "language" in data:
                    language = data['language']
                    entity['language'] = str(language)
                if "page" in data:
                    page = data['page']
                    entity['page'] = int(page)
                if "title" in data:
                    title = data['title']
                    entity['title'] = str(title)
                if "year" in data:
                    year = data['year']
                    entity['year'] = int(year)
                dict1['isbn'] = str(entity['isbn'])
                dict1['author'] = str(entity['author'])
                dict1['image_public_url'] = entity['image_public_url']
                dict1['language'] = str(entity['language'])
                dict1['title'] = str(entity['title'])
                dict1['page'] = int(entity['page'])
                dict1['year'] = int(entity['year'])
                json_array.append(dict1)
                datastore_client.put(entity)
        if dict1 is None:
            return "book not found", 404
        return jsonify(json_array), 200


    if request.method == 'DELETE':
        datastore_client = datastore.Client.from_service_account_json('library-api-348504-fdb7b25a3b02.json')
        query = datastore_client.query(kind='Books')
        book_entities = list(query.fetch())
        for entity in book_entities:
            if entity['isbn'] == isbn:
                datastore_client.delete(entity)
                return "Success delete", 204

@app.route("/api/health", methods=['GET'])
@require_api_key
def email():
    requests.post(
    "https://api.mailgun.net/v3/sandbox7f7f57d2ad9e4245bd362c756a609256.mailgun.org/messages",
		auth=("api", "0fe0ede08f86e9e24f0ee1f1f2258afb-fe066263-88a36dee"),
		data={"from": "Chengyue <chengyuel@uchicago.edu>",
			"to": "email <j3a5d7z8r7i6q2y8@mpcs52555-2022-spring.slack.com>",
			"subject": "👍 Health Check - https://library-api-348504.uc.r.appspot.com/ ",
			"text": "Health check!"})
    return "email sent", 200

if __name__ == '__main__':
    app.run(debug=True)
