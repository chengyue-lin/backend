# Photo Timeline Backend

###### App Engine Flask Application with Google Cloud Storage

> Running this application requires setting up the project initially with a non-@uchicago.edu account. Use your personal gmail and then add your @uchicago.edu account as an owner.


# URL
URL=https://prefab-mapper-347607.uc.r.appspot.com/

# Homepage
curl https://prefab-mapper-347607.uc.r.appspot.com/

# Get all dog data
curl https://prefab-mapper-347607.uc.r.appspot.com/dogs

# Post a new image
curl -X POST \
  -H "Content-Type:multipart/form-data" \
  -F "file=@dog4.jpg" \
  -F "star_rating=10"  \
  https://prefab-mapper-347607.uc.r.appspot.com/upload

# Test 404
curl https://prefab-mapper-347607.uc.r.appspot.com/cats