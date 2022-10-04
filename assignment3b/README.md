# Book Library Backend
# Assignment 3b
#### Name: Chengyue Lin
#### email: chengyuel@uchicago.edu

# URL
URL= https://book-library-api-348006.uc.r.appspot.com/

## post books/\<isbn>
curl -X POST -H "Content-Type: multipart/form-data" -F "data={\"author\": \"John\",\"language\": \"English\",\"page\": \"300\",\"title\": \"Sunset\",\"year\": \"1990\"}; type=application/json" -F "file=@dog4.jpg" https://book-library-api-348006.uc.r.appspot.com/books/{isbn}

## post books
curl -X POST -H "Content-Type: multipart/form-data" -F "data={\"author\": \"John\",\"language\": \"English\",\"page\": \"300\",\"title\": \"Sunset\",\"year\": \"1990\"}; type=application/json" -F "file=@dog4.jpg" https://book-library-api-348006.uc.r.appspot.com/books

## delete books/\<isbn>
curl -X DELETE https://book-library-api-348006.uc.r.appspot.com/books/{isbn}

## get books/\<isbn>
curl -X GET https://book-library-api-348006.uc.r.appspot.com/books/{isbn}

##get books
curl -X GET https://book-library-api-348006.uc.r.appspot.com/books?author=John
### OR
curl -X GET https://book-library-api-348006.uc.r.appspot.com/books?language=english
### OR
curl -X GET "https://book-library-api-348006.uc.r.appspot.com/books?author=John&language=english"
### OR
curl -X GET https://book-library-api-348006.uc.r.appspot.com/books?flexible=in

## put books/\<isbn>
curl -X PUT -H "Content-Type: multipart/form-data" -F "data={\"language\": \"Chinese\",\"page\": \"789\",\"year\": \"1999\"}; type=application/json" https://book-library-api-348006.uc.r.appspot.com/books/{isbn}



