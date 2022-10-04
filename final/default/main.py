from flask import Flask, request, jsonify, render_template, abort
from google.cloud import datastore

app = Flask(__name__)

@app.route("/", methods=['GET'])
def default():
    datastore_client = datastore.Client.from_service_account_json('final-project-350706-0692d343a294.json')
    query = datastore_client.query(kind='staffs')
    staffs = list(query.fetch())
    json_array=[]
    for each in staffs:
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
if __name__ == '__main__':
    app.run(debug=True, port=8000)