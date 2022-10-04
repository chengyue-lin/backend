import os, json
from flask import Flask, request, jsonify, render_template
from google.cloud import datastore
from google.cloud import storage

app = Flask(__name__)


@app.route("/analytics/dashboard")
def analytics():
    datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')

    query = datastore_client.query(kind='staffs')
    staffs = list(query.fetch())
    return render_template('homepage.html', staffs=staffs)

@app.route("/analytics/upload", methods=['POST'])
def upload():
    staffid = request.form["staffid"]
    name = request.form["name"]
    title = request.form["title"]
    email = request.form["email"]
    phone = request.form["phone"]
    salary = request.form["salary"]
    score = request.form["score"]
    photo = request.files['file']
    storage_client = storage.Client.from_service_account_json('final-project-350706-0692d343a294.json')
    bucket_name = "human-resource-manage"
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

    return render_template('success.html')

@app.route("/analytics/search", methods=['GET'])
def search():
    datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
    if request.args.get("name") != "" and request.args.get("title") != "":
        query = datastore_client.query(kind='staffs')
        query.add_filter("name", "=", request.args.get("name"))
        query.add_filter("title", "=", request.args.get("title"))
        staffs = list(query.fetch())
        return render_template('result.html', staffs=staffs)
    elif request.args.get("name") != "":
        query = datastore_client.query(kind='staffs')
        query.add_filter("name", "=", request.args.get("name"))
        staffs = list(query.fetch())
        return render_template('result.html', staffs=staffs)
    elif request.args.get("title") != "":
        query = datastore_client.query(kind='staffs')
        query.add_filter("title", "=", request.args.get("title"))
        staffs = list(query.fetch())
        return render_template('result.html', staffs=staffs)
    else:
        query = datastore_client.query(kind='staffs')
        staffs = list(query.fetch())
        return render_template('result.html', staffs=staffs)

@app.route("/analytics/update", methods=['POST'])
def update():
    datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
    id = request.form["staffid"]
    query = datastore_client.query(kind='staffs')
    query.add_filter("staffid", "=", id)
    staffs = list(query.fetch())
    if len(staffs) ==0:
        return render_template('noExist.html')
    name = request.form["name"]
    title = request.form["title"]
    email = request.form["email"]
    phone = request.form["phone"]
    salary = request.form["salary"]
    score = request.form["score"]
    for entity in staffs:
        if name !="":
            entity['name'] = str(name)
        if email != "":
            entity['email'] = str(email)
        if title != "":
            entity['title'] = str(title)
        if phone != "":
            entity['phone'] = str(phone)
        if salary != "":
            entity['salary'] = int(salary)
        if score != "":
            entity['score'] = int(score)
        datastore_client.put(entity)

    return render_template('success.html')

@app.route("/analytics/delete", methods=['POST'])
def delete():
    datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
    id = request.form["staffid"]
    query = datastore_client.query(kind='staffs')
    query.add_filter("staffid", "=", id)
    staffs = list(query.fetch())
    if len(staffs) == 0:
        return render_template('noExist.html')
    for entity in staffs:
        datastore_client.delete(entity)
    return render_template('success.html')

@app.route("/analytics/tax", methods=['GET'])
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
    staffs = json_array
    return render_template('tax.html', staffs= staffs)

@app.route("/analytics/balance", methods=['POST'])
def balance():
    income = int(request.form["income"])
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
        staffs = json_array
        return render_template('result.html', staffs=staffs)
if __name__ == '__main__':
    app.run(debug=True)