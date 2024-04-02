# Creator: Israel Showell
# Start Date: 3/29/2024
# End Date: 4/2/2024
# Project: Register and Login Website 
# Version: 1.00

# Description:
"""
This is a GUI login project that uses SQLite as its database system. <br>
This project is a way for me to practice GUI and Flask development, linking HTML/CSS Frontend and Python Backend,
and database management actions including, but not limited to; 

- Accessing databases 
- Creating tables inside databases 
- Inserting data into the tables 
- Checking the contents of tables
- Connecting Front-Ends and Back-Ends together
This script handles the submission form for registering.
"""
#These are the imported libaries I am using to make the program
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,IntegerField,TextAreaField,SubmitField
from wtforms.validators import ValidationError, DataRequired

#Here, I create a form format that will be rendered by app.py and by the HTML page
class PingPongTournamentRegistrationForm(FlaskForm):
    #Creates the username field and requires users to use it.
    Username=StringField(label="Username",validators=[DataRequired()])
    #Creates the password field and requires users to use it.
    Password=PasswordField(label="Password",validators=[DataRequired()])
    #Creates the phone field and requires users to use it.
    PhoneNumber=IntegerField(label="Enter Mobile Number",validators=[DataRequired()])
    #Creates the Gender field 
    Gender=StringField(label="Gender")
    #Creates the address TextAreaField 
    Address=TextAreaField(label="Address")
    #Creates the username field and requires users to use it.
    Age=IntegerField(label="Age")
    #Creates the button for users to submit their form
    Submit=SubmitField(label="Send")

#End of Script
