# Python Django Assignment

# Installation instructions
1) Install Docker
   1) Install docker depending on your OS
   2) run: "docker-compose up" to start postgres
2) Install django 
   1) python3 -m venv env
   2) source env/bin/activate
   3) pip install -r requirements.txt
3) Create supper user
   1) python manage.py createsuperuser
4) Add email credentials in settings.py

# Rest APIS

   Methods &nbsp; URL &nbsp; Actions &nbsp; Body

   GET &nbsp; api/students &nbsp; get all Students

   GET &nbsp; api/students/:id &nbsp; get Student by id

   POST &nbsp; api/students &nbsp; add new student &nbsp; { "name": "NAME","faculty_name": "FACULTY","number": "NUMBER","email": "EMAIL","date_of_birth": "DOB"}

   PUT &nbsp; api/students/:id &nbsp; update Student by id &nbsp; { "name": "NAME","faculty_name": "FACULTY","number": "NUMBER","email": "EMAIL","date_of_birth": "DOB"}

   DELETE &nbsp; api/students/:id &nbsp; remove Student by id

   GET &nbsp; api/students?name=[kw] &nbsp; find all Students which name contains 'kw'
   
   GET &nbsp; api/students?age=[num] &nbsp; find all Students age less than provided number
   
   POST &nbsp; api/students/send-email &nbsp; send email to students &nbsp; { "subject": "SUBJECT","text": "TEXT","html": "HTML","recipient_list": ["LIST OF EMAILS"]}
   
   POST &nbsp; token/ &nbsp; to get access token &nbsp; {"username": "USERNAME","password": "PASSWORD"}
   
