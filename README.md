# News-Highlights

## Author
### *Gloria Givondo* (19/11/2018)

## Description 
Pitcher is an application that displays pitches from various categories e.g. Promotion, Pick-Up lines. The user is able to view these pitches but once they are loged in they can leave a comment, upvote and downvote and view their pitches on their profile page .

You can view the live link on: https://pitch-time.herokuapp.com/

## User Stories
These are the behaviours that the application implenents for use by a user.

As a user, I would like: 

* To see the pitches other people have posted.
* To vote on the pitch they liked and give it a downvote or upvote.
* To be signed in for me to leave a comment
* To receive a welcoming email once I sign up.
* To view the pitches I have created in my profile page.
* To comment on the different pitches and leave feedback.
* To submit a pitch in any category.
* To view the different categories.

## Setup / Installation Requirements
* Web browser
* Virtual environment
* Flask
* Python version 3.6


### Cloning the Repo
* In your terminal run:

        $ git clone https://github.com/GeGe-K/News-Highlights.git
        $ cd Pitcher

## Running the Application 
* Create the virtual environment

        $ sudo apt-get install python3.6 -venv
        $ python3.6 -m venv virtual

* Activate virtual environment

        $ source virtual/bin/activate

* Install Flask and other Modules

        $ pip install -r requirements.txt

* Set up the environment variables
        
Create a start.sh file and paste the following.
`export SECRET_KEY='<secret_key>'`
`export MAIL_USERNAME='<username>'`
`export MAIL_PASSWORD='<password>'`

* Run the application in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application 
* To run the tests for the class files and check if they function well:

        $ python3.6 manage.py tests

## Technologies Used
* Virtual environment
* Flask
* Python version 3.6
* Flask-Bootstrap4
* Pip
* HTML
* CSS
* Heroku
* Visual Studio Editor

## Known Bugs
There are no known bugs. Contact gloriagivondo@gmail.com in-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Gloria**

