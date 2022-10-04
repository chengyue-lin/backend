import os, json

import requests
from flask import Flask, request, jsonify, render_template, abort
from google.cloud import storage
from google.cloud import datastore


app = Flask(__name__)

CLOUD_STORAGE_BUCKET = "library-api"


@app.route("/tasks", methods=['GET'])
def send_email():
    my_header = {'X-Api-Key': 'abcdef123456'}
    requests.get('https://library-api-348504.uc.r.appspot.com/api/health', headers=my_header)
    return "request sent",200

if __name__ == '__main__':
    app.run(debug=True)
