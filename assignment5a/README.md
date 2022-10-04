# Book Library Backend
# Assignment 5-a
#### Name: Chengyue Lin
#### email: chengyuel@uchicago.edu

# URL
URL= https://library-api-348504.uc.r.appspot.com/

## post /api/books/\<isbn>
curl -X POST -H 'X-Api-Key: abcdef123456' -H "Content-Type: multipart/form-data" -F "data={\"author\": \"John\",\"language\": \"English\",\"page\": \"300\",\"title\": \"Sunset\",\"year\": \"1990\"}; type=application/json" -F "file=@dog4.jpg" https://library-api-348504.uc.r.appspot.com/books/{isbn}

## post /api/books
curl -X POST -H 'X-Api-Key: abcdef123456' -H "Content-Type: multipart/form-data" -F "data={\"author\": \"John\",\"language\": \"English\",\"page\": \"300\",\"title\": \"Sunset\",\"year\": \"1990\"}; type=application/json" -F "file=@dog4.jpg" https://library-api-348504.uc.r.appspot.com/books

## delete /api/books/\<isbn>
curl -X DELETE -H 'X-Api-Key: abcdef123456' https://library-api-348504.uc.r.appspot.com/books/{isbn}

## get /api/books/\<isbn>
curl -X GET -H 'X-Api-Key: abcdef123456' https://library-api-348504.uc.r.appspot.com/books/{isbn}

## get /api/books 
curl -X GET -H 'X-Api-Key: abcdef123456' https://library-api-348504.uc.r.appspot.com/books?author=John
### OR
curl -X GET -H 'X-Api-Key: abcdef123456' https://library-api-348504.uc.r.appspot.com/books?language=english
### OR
curl -X GET -H 'X-Api-Key: abcdef123456' "https://library-api-348504.uc.r.appspot.com/books?author=John&language=english"
### OR
curl -X GET -H 'X-Api-Key: abcdef123456' https://library-api-348504.uc.r.appspot.com/books?flexible=in

## put /api/books/\<isbn>
curl -X PUT -H 'X-Api-Key: abcdef123456' -H "Content-Type: multipart/form-data" -F "data={\"language\": \"Chinese\",\"page\": \"789\",\"year\": \"1999\"}; type=application/json" https://library-api-348504.uc.r.appspot.com/books/{isbn}

## analytics
https://analytics-dot-library-api-348504.uc.r.appspot.com
### display dashboard
https://analytics-dot-library-api-348504.uc.r.appspot.com/analytics/dashboard

## api
https://api-dot-library-api-348504.uc.r.appspot.com

## tasks
https://tasks-dot-library-api-348504.uc.r.appspot.com




