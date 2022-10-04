### /api/staffs:
    get:
        summary: Return a Json array of human information object
        parameters:
            name(option) - filter people list by name
            title(option) - filter people list by job title
            don't have any parameter will return all people information. 
    
    post: 
        summary: post a new staff information
        payload:
            a people infomation object

### /api/staffs/<staffid>:
    get: 
        summary: return a json object with the particular staffid value, error occur when staffid not exist

    put:
        summary: update information for the particular staffid value.
        payload:
            a people information object (can be only the field that need to update)

    delete:
        summary: delete a people information with the particular staffid value.

### /api/tax:
    get:
        summary: return a json object with all people need to pay for the tax(which is 10 percent of salary)

### /api/fired:
    get:
        summary: return a json object with a low performance score that need to be fired, since the total income is less than the total salary
        parameter: 
            income(necessary) - a value that represent total income for company

