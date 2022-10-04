## post a new staff information
curl -X POST -H "X-Api-Key: abcdef123456" -H "Content-Type: multipart/form-data"  -F "data={\\"staffid\\": \\"0000000\\",\\"name\\": \\"John\\",\\"title\\": \\"CEO\\",\\"email\\": \\"john@human.com\\",\\"phone\\": \\"818-000-1234\\",\\"salary\\":\\"6500\\",\\"score\\": \\"100\\"}; type=application/json" -F "file=@staff.jpg" "https://final-project-350706.uc.r.appspot.com/api/staffs"

## GET ALL staffs information
curl -X GET -H "X-Api-Key: abcdef123456"  "https://final-project-350706.uc.r.appspot.com/api/staffs"

## GET the staff name with "Sam"
curl -X GET -H "X-Api-Key: abcdef123456"  "https://final-project-350706.uc.r.appspot.com/api/staffs?name=Sam"

## GET the staff job title with "intern"
curl -X GET -H "X-Api-Key: abcdef123456"  "https://final-project-350706.uc.r.appspot.com/api/staffs?title=intern"

## GET the staff name with "jim" and job title with "intern"
curl -X GET -H "X-Api-Key: abcdef123456"  "https://final-project-350706.uc.r.appspot.com/api/staffs?name=jim&title=intern"

## GET the staff information for the particular staffID
curl -X GET -H "X-Api-Key: abcdef123456" "https://final-project-350706.uc.r.appspot.com/api/staffs/0000000" 

## DELETE the staff information for the particular staffID
curl -X DELETE -H "X-Api-Key: abcdef123456" "https://final-project-350706.uc.r.appspot.com/api/staffs/0000000" 

## PUT the staff information for the particular staffID
curl -X PUT -H "X-Api-Key: abcdef123456" -H "Content-Type: multipart/form-data"  -F "data={\"phone\": \"818-000-5890\",\"salary\": \"7000\",\"score\": \"99\"}; type=application/json" "https://final-project-350706.uc.r.appspot.com/api/staffs/0000000"

## GET the tax information that need to pay for each staff
curl -X GET -H "X-Api-Key: abcdef123456" "https://final-project-350706.uc.r.appspot.com/api/tax"

## GET the low performance score staff information that when income is less than total salary
curl -X GET -H "X-Api-Key: abcdef123456" "https://final-project-350706.uc.r.appspot.com/api/fired?income=100500"


