# Book Library Backend
# Assignment 4
#### Name: Chengyue Lin
#### email: chengyuel@uchicago.edu

# URL
URL= https://library-api-348504.uc.r.appspot.com/

## post books/\<isbn>
curl -X POST -H "Content-Type: multipart/form-data" -F "data={\"author\": \"John\",\"language\": \"English\",\"page\": \"300\",\"title\": \"Sunset\",\"year\": \"1990\"}; type=application/json" -F "file=@dog4.jpg" https://library-api-348504.uc.r.appspot.com/books/{isbn}

## post books
curl -X POST -H "Content-Type: multipart/form-data" -F "data={\"author\": \"John\",\"language\": \"English\",\"page\": \"300\",\"title\": \"Sunset\",\"year\": \"1990\"}; type=application/json" -F "file=@dog4.jpg" https://library-api-348504.uc.r.appspot.com/books

## delete books/\<isbn>
curl -X DELETE https://library-api-348504.uc.r.appspot.com/books/{isbn}

## get books/\<isbn>
curl -X GET https://library-api-348504.uc.r.appspot.com/books/{isbn}

## get books 
curl -X GET https://library-api-348504.uc.r.appspot.com/books?author=John
### OR
curl -X GET https://library-api-348504.uc.r.appspot.com/books?language=english
### OR
curl -X GET "https://library-api-348504.uc.r.appspot.com/books?author=John&language=english"
### OR
curl -X GET https://library-api-348504.uc.r.appspot.com/books?flexible=in

## put books/\<isbn>
curl -X PUT -H "Content-Type: multipart/form-data" -F "data={\"language\": \"Chinese\",\"page\": \"789\",\"year\": \"1999\"}; type=application/json" https://library-api-348504.uc.r.appspot.com/books/{isbn}



