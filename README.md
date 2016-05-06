## PairProgram
##### Andela Kenya Class VII Boot Camp Project

PairProgram is a pair programming app powered by Flask, Firebase and Firepad. It facilitates multiple programmers to work on the same code file in real time.

### Required features

* A user is able to login and sign up.
* A user can create a new pair programming sessions.
* A user can edit and delete a pair programming session.
* A user can invite other users of the app to a pair session.
* Within a pair programming session the user can:
	* Write code within editor
	* Chat with other users on the session

## An instance of PairProgram on your machine

1. Clone this repository

`git clone https://github.com/JoyWangari/bc-7-pair-programming.git`

2. Do a pip install for the dependancies

`pip install -r requirements.txt`

3. Initialize your database and migrate the database models.

`python manage.py db init`
`python manage.py db upgrade`

4. THen finally, run a development server.

`python manage.py runserver`

## Issues

* Deleting sessions is not working at the moment.
* Chatting functionality has yet to be implemented.
* Issues with the invite.

