curl -s GET https://api.vatcomply.com/vat?vat_number=NL810462783B01 HTTP/1.1 | jq  #check the vat number valid or not

curl -s GET https://api.vatcomply.com/rates HTTP/1.1 | jq # get the exchange rate for today

curl -s GET https://api.vatcomply.com/rates?base=USD HTTP/1.1 | jq # change the base currency to USD

curl -s GET https://api.vatcomply.com/rates?date=2000-04-05 HTTP/1.1 | jq # check previous date exchange rate

curl -s GET https://api.vatcomply.com/currencies HTTP/1.1 | jq # check the currencies name and symbol

curl -s GET https://api.vatcomply.com/geolocate HTTP/1.1 | jq # get the geolocation by IP address to determine what currency we are going to use
