# Creator: Israel Showell
# Start Date: 3/29/2024
# End Date: 4/2/2024
# Project: Register-Login-Website
# Version: 1.00

#Description:
This will be a mock website where a user can register an account with a username and password, and then login into their account.
This is a mock website register/login project that uses SQLite as its database system, HTML/CSS Front-End, and Python as its Back-End. <br>
This project is a way for me to practice Flask development, linking HTML/CSS Front-End to Python Back-End,
and database management actions including, but not limited to; 

- Accessing databases 
- Creating tables inside databases 
- Inserting data into the tables 
- Checking the contents of tables
- Connecting Front-Ends and Back-Ends together

# Version History:
# V-1.00: (3/29-4/2/2024)
Initial Version <br>
Uploaded to Github


# Packages Used as of V-1.00:
Package      Version
------------ -------
blinker      1.7.0
click        8.1.7
colorama     0.4.6
Flask        3.0.2
Flask-WTF    1.2.1
itsdangerous 2.1.2
Jinja2       3.1.3
MarkupSafe   2.1.5
pip          22.0.4
setuptools   58.1.0
Werkzeug     3.0.1
WTForms      3.1.2

# Current Features as of V-1.00:
- Program creates and connects to a database and creates a table if necessary
- A user can enter in a username and password to login 
- If they exist, they will be sent to a dashboard page, otherwise, they will be taken to the register page
- A user can register a profile with a username and password using a FlaskForm
- If the user tries to create an account that exists already, they will be not be logged in

# Future Features to Implement:
- Display all information about the user who is logged in
- Improve the UI for the user
- Host this program on a server so people on the internet can find and register online

