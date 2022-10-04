import os, json
from functools import wraps
from flask import Flask, request, jsonify, render_template, abort
from google.cloud import storage
from google.cloud import datastore
import logging

app = Flask(__name__)
CLOUD_STORAGE_BUCKET = "human-resource-manage"


@app.errorhandler(405)
def book_not_found(e):
    logging.error("Can't find the staff ID")
    return "Can't find the staff ID.", 405

@app.errorhandler(406)
def isbn_invalid(e):
    logging.error("staff ID number is invalid")
    return "staff ID number is invalid.", 406

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get("X-Api-Key") != "abcdef123456":
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/api/staffs", methods=['GET', 'POST'])
@require_api_key
def staff():
    if request.method == "GET":
        datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
        if request.args.get("name") is not None and request.args.get("title") is not None:
            query= datastore_client.query(kind='staffs')
            query.add_filter("name", "=", request.args.get('name'))
            query.add_filter("title", "=", request.args.get('title'))
            query_iter = list(query.fetch())
            json_array = []
            for each in query_iter:
                dict = {}
                dict['staffid'] = each['staffid']
                dict['name'] = each['name']
                dict['title'] = each['title']
                dict['email'] = each['email']
                dict['phone'] = each['phone']
                dict['salary'] = each['salary']
                dict['score'] = each['score']
                dict['photo_url'] = each['photo_url']
                json_array.append(dict)
            return jsonify(json_array), 200
        elif request.args.get("name") is not None :
            query= datastore_client.query(kind='staffs')
            query.add_filter("name", "=", request.args.get('name'))
            query_iter = list(query.fetch())
            json_array = []
            for each in query_iter:
                dict = {}
                dict['staffid'] = each['staffid']
                dict['name'] = each['name']
                dict['title'] = each['title']
                dict['email'] = each['email']
                dict['phone'] = each['phone']
                dict['salary'] = each['salary']
                dict['score'] = each['score']
                dict['photo_url'] = each['photo_url']
                json_array.append(dict)
            return jsonify(json_array), 200
        elif request.args.get("title") is not None:
            query= datastore_client.query(kind='staffs')
            query.add_filter("title", "=", request.args.get('title'))
            query_iter = list(query.fetch())
            json_array = []
            for each in query_iter:
                dict = {}
                dict['staffid'] = each['staffid']
                dict['name'] = each['name']
                dict['title'] = each['title']
                dict['email'] = each['email']
                dict['phone'] = each['phone']
                dict['salary'] = each['salary']
                dict['score'] = each['score']
                dict['photo_url'] = each['photo_url']
                json_array.append(dict)
            return jsonify(json_array), 200
        else:
            query = datastore_client.query(kind='staffs')
            query_iter = list(query.fetch())
            json_array = []
            for each in query_iter:
                dict = {}
                dict['staffid'] = each['staffid']
                dict['name'] = each['name']
                dict['title'] = each['title']
                dict['email'] = each['email']
                dict['phone'] = each['phone']
                dict['salary'] = each['salary']
                dict['score'] = each['score']
                dict['photo_url'] = each['photo_url']
                json_array.append(dict)
            return jsonify(json_array), 200
    if request.method == "POST":
        string_json = request.form["data"]
        data = json.loads(string_json)
        photo = request.files['file']
        staffid = data['staffid']
        name = data['name']
        title = data['title']
        email = data['email']
        phone = data['phone']
        salary = data['salary']
        score = data['score']
        storage_client = storage.Client.from_service_account_json('final-project-350706-0692d343a294.json')
        bucket_name = CLOUD_STORAGE_BUCKET
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(photo.filename)
        blob.upload_from_string(photo.read(), content_type=photo.content_type)
        datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
        kind = 'staffs'
        key = datastore_client.key(kind)
        entity = datastore.Entity(key)
        entity['staffid'] = str(staffid) if staffid else "no provide"
        entity['name'] = str(name) if name else "no provide"
        entity['email'] = str(email) if email else "no provide"
        entity['title'] = str(title) if title else "no provide"
        entity['phone'] = str(phone) if phone else "no provide"
        entity['salary'] = int(salary) if salary else 500
        entity['score'] = int(score) if score else 5
        entity['photo_url'] = blob.public_url
        datastore_client.put(entity)

        return "post a new staff information", 201

@app.route("/api/staffs/<staffid>", methods=['GET',  'PUT', 'DELETE'])
@require_api_key
def operation(staffid):
    if request.method == 'GET':
        if not str(staffid).isdigit() or len(staffid) != 7:
            return "invalid staff ID, staff ID should only have 7 digit", 406
        datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
        query = datastore_client.query(kind='staffs')
        query_iter = list(query.fetch())
        json_array = []
        dict1 = {}
        for each in query_iter:
            if each['staffid'] ==staffid:
                dict1['staffid'] = each['staffid']
                dict1['name'] = each['name']
                dict1['title'] = each['title']
                dict1['email'] = each['email']
                dict1['phone'] = each['phone']
                dict1['salary'] = each['salary']
                dict1['score'] = each['score']
                dict1['photo_url'] = each['photo_url']
                json_array.append(dict1)
        if dict1 is None:
            return "Don't exist that staffid", 405
        return jsonify(json_array), 202

    if request.method == 'PUT':
        if not str(staffid).isdigit() or len(staffid) != 7:
            return "invalid staff ID", 406
        string_json = request.form["data"]
        data = json.loads(string_json)
        datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
        query = datastore_client.query(kind='staffs')
        query_iter = list(query.fetch())
        json_array = []
        dict1 = {}
        for each in query_iter:

            if each['staffid'] == staffid:
                print(each)
                if "name" in data:
                    name = data['name']
                    each['name'] = str(name)
                if "title" in data:
                    title = data['title']
                    each['title'] = str(title)
                if "email" in data:
                    email = data['email']
                    each['email'] = str(email)
                if "phone" in data:
                    phone = data['phone']
                    each['phone'] = str(phone)
                if "salary" in data:
                    salary = data['salary']
                    each['salary'] = int(salary)
                if "score" in data:
                    score = data['score']
                    each['score'] = int(score)
                print(each)
                dict1['staffid'] = str(each['staffid'])
                dict1['name'] = str(each['name'])
                dict1['photo_url'] = each['photo_url']
                dict1['email'] = str(each['email'])
                dict1['title'] = str(each['title'])
                dict1['phone'] = str(each['phone'])
                dict1['salary'] = int(each['salary'])
                dict1['score'] = int(each['score'])
                print(dict1)
                json_array.append(dict1)
                datastore_client.put(each)
        if dict1 is None:
            return "Don't exist staffid", 405
        return jsonify(json_array), 203

    if request.method == 'DELETE':
        if not str(staffid).isdigit() or len(staffid) != 7:
            return "invalid staff ID", 406
        datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
        query = datastore_client.query(kind='staffs')
        book_entities = list(query.fetch())
        for entity in book_entities:
            if entity['staffid'] == staffid:
                datastore_client.delete(entity)
                return "Success delete", 204
        return "Can't found staff", 405

@app.route("/api/tax", methods=['GET'])
@require_api_key
def tax():
    datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
    query = datastore_client.query(kind='staffs')
    query_iter = list(query.fetch())
    json_array = []
    for each in query_iter:
        dict = {}
        dict['staffid'] = each['staffid']
        dict['name'] = each['name']
        dict['salary'] = each['salary']
        tax = each['salary'] * 0.10
        dict['tax'] = tax
        json_array.append(dict)
    return jsonify(json_array), 205

@app.route("/api/fired", methods=['GET'])
@require_api_key
def fire():
    income = int(request.args.get("income"))
    datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
    query = datastore_client.query(kind='staffs')
    query.order = ["score"]
    query_iter = list(query.fetch())
    total_salary = 0
    for each in query_iter:
        total_salary += each['salary']
    if total_salary > income:
        json_array = []
        for each in query_iter:
            dict = {}
            dict['staffid'] = each['staffid']
            dict['name'] = each['name']
            dict['title'] = each['title']
            dict['email'] = each['email']
            dict['phone'] = each['phone']
            dict['salary'] = each['salary']
            dict['score'] = each['score']
            dict['photo_url'] = each['photo_url']
            total_salary -= each['salary']
            json_array.append(dict)
            if total_salary <= income:
                break
        return jsonify(json_array), 206
    else:
        return "Total income greater than total salary no one will be fired.", 207
if __name__ == '__main__':
    app.run(debug=True, port=8000)
