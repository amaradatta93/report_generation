lone the repository

#Setup:
This application uses python 3.5.
Install virtual environment: `pip install virtualenv`
Create a virtual environment using: `virtualenv -p python3 env`
Activate virtual env: `source env/bin/activate`
Install requirements: `pip install -r requirements.txt`

#Prepare the database
Configure the MySQL in settings.py, or set the `DATABASE_URL` environment variable in the format `mysql://username:password@host:port/dbname`.
Or run the authorization file obtained - `source auth.sh`
`python manage.py makemigrations`
`python manage.py migrate`

#Start the server
`python manage.py runserver`

