# Registration Form 
The purpose of this assignment was to practice using flash in Flask by validating a registration form. 
The registration page contains the following fields: 
* email
* first_name
* last_name
* birthday
* password
* confirm_password
The validation included are: 
* All fields are required and must not be blank
* Email should be a valid email
* First and last name cannot contain any numbers 
* Birthday must be in the past
* Password should be ore than 8 characters
* Password and confirmed password must match 
* Password must contain at least 1 uppercase and 1 numeric value 
When the form is submitted, the page is redirected back to root. If there were errors, the messages will 
show up in red. If there were no errors, there will be a "Success!" message in green. 