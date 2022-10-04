WEB_API_KEY="AIzaSyA1KWinhJgvxPTN-w379gWvM1YR1j2dzWQ"

# https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=[API_KEY]

curl "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=${WEB_API_KEY}" \
    -H 'Content-Type: application/json' \
    --data-binary '{"email":"scoobydoo@dogs.com","password":"snack1234","returnSecureToken":true}'
