# Assignment 6
# Name: Chengyue Lin
# Email: chengyuel@uchicago.edu

### sign up email
curl https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyA1KWinhJgvxPTN-w379gWvM1YR1j2dzWQ -H 'Content-Type: application/json' --data-binary '{"email":"test@uchicago.com","password":"abc123456","returnSecureToken":true}'

### sign in email
curl "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyA1KWinhJgvxPTN-w379gWvM1YR1j2dzWQ" -H 'Content-Type:application/json' --data-binary '{"email":"scoobydoo@dogs.com","password":"snack1234","returnSecureToken":true}'

#### For the cloud function, I uploaded the index.ts file in my repo. And it will call when we create a new isbn number in the firebase database. 

##### No command line work for the CRUD. (get, post, delete, update)

