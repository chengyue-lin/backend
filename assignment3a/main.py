import os, datetime, json
from flask import Flask, request, jsonify
from google.cloud import storage
from google.cloud import datastore

app = Flask(__name__)

CLOUD_STORAGE_BUCKET = "photo_timeline-shared"


@app.route("/")
def homepage():
  return "Hello Photo Timeline!", 200


@app.errorhandler(404)
def page_not_found(e):
    return "Dog not found.", 404

"""Dogs Endpoint"""
@app.route("/dogs")
def dogs():
  datastore_client = datastore.Client.from_service_account_json('prefab-mapper-347607-92858260c7d1.json')
  query = datastore_client.query(kind='Photos')
  photo_entities = list(query.fetch())

  json_array=[]
  for entity in photo_entities:
    dict = {}
    dict['blob_name'] = entity['blob_name']
    dict['image_public_url'] = entity['image_public_url']
    dict['timestamp'] = str(entity['timestamp'])
    dict['star_rating'] = entity['star_rating']
    json_array.append(dict)
  return jsonify(json_array), 200


@app.route("/upload", methods=['POST'])
def upload():
  photo = request.files['file']
  star_rating = request.form['star_rating']
  storage_client = storage.Client.from_service_account_json('prefab-mapper-347607-92858260c7d1.json')
  bucket_name = CLOUD_STORAGE_BUCKET
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(photo.filename)
  blob.upload_from_string(photo.read(), content_type=photo.content_type)
  print(f"File uploaded: {photo.filename} to {blob.public_url}")

  datastore_client = datastore.Client.from_service_account_json('prefab-mapper-347607-92858260c7d1.json')
  kind = 'Photos'
  name = blob.name
  key = datastore_client.key(kind, name)
  entity = datastore.Entity(key)
  entity['blob_name'] = blob.name
  entity['image_public_url'] = blob.public_url
  entity['timestamp'] = datetime.datetime.now()
  entity['star_rating'] = star_rating

  datastore_client.put(entity)
  return ":)", 201


if __name__ == '__main__':
  app.run(debug=True)
