# Creator: Israel Showell
# Start Date: 3/29/2024
# End Date: 4/2/2024
# Project: Register and Login Website 
# Version: 1.20

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
This is the main script where everything comes together to run.
"""
#These are the imported libaries I am using to make the program
from flask import Flask, render_template, request
from formsubmission import PingPongTournamentRegistrationForm
import sqlite3

#Important variables and objects
#Requried by Flask to detect the app when running 'flask run'
app=Flask(__name__)
#This is used to help protect data being sent by the app.
#This protection is used to defend against CSRF attacks.
#(Cross-Site Request Forgery)
app.secret_key="__privatekey__"

#All HTML files are located in the 'templates' because that is where render_template looks for HTML files

#The Home Page is located as the root of the web page
@app.route('/')
def Home():
    #Home is referenced in the HTML files
    return render_template('Home.html')

#The Login Page is able to detect POST and GET requests
#POST sends data, GET gets data
@app.route('/login', methods=['POST','GET'])
def login():
    #When the button is pressed, the user makes the page send a POST request
    if request.method=='POST':
        #Saves the request's data in variables
        userName = request.form['Username']
        passWord = request.form['Password']

        #Then it connects to the database
        con = sqlite3.connect('users.db')
        #c serves as a database cursor, a control structure that enables traversal over the records in a database
        c = con.cursor()

        #statement holds an SQL Query for the users table in the users database
        #This query checks to see if the user and password entered exist in the database
        statement=f"SELECT * from users WHERE Username='{userName}' AND Password='{passWord}';"

        #We then tell the cursor to run the query
        c.execute(statement)
        #c.fetchone fetchs the next row of a query resultand returns a single tuple,
        #Or None if no more rows are available.
        if not c.fetchone():
            #If the user and password is not found, the program will not sign them in
            return render_template("login.html")
        else:
            #If the login is right, they go to the dashboard page, and their name is displayed
            return render_template('dashboard.html', name=userName)
    else:
        #If the user is just going to the login page, the page is rendered by the program
         request.method=='GET'
         return render_template("login.html")


#The registrationForm Page is able to detect POST and GET requests
#POST sends data, GET gets data
@app.route('/registrationform', methods=['POST','GET']) 
def registrationForm():
    #This creates an object named PingPong based off of the form defined in the formsubmission module
    PingPong = PingPongTournamentRegistrationForm()

    #The program connects to the database
    db2=sqlite3.connect('users.db')
    #c serves as a database cursor, a control structure that enables traversal over the records in a database
    c=db2.cursor()

    #When the button is pressed, the user makes the page send a POST request
    if request.method=='POST':
        #Checks to make sure the user didn't leave the Username and Password fields blank
        if(request.form["Username"]!="" and request.form["Password"]!=""):
            #Saves the request's data in variables
            userName = request.form['Username']
            passWord = request.form['Password']

            #statement holds an SQL Query for the users table in the users database
            #This query checks to see if the user and password entered exist in the database
            statement=f"SELECT * from users WHERE Username='{userName}' AND Password='{passWord}';"

            #We then tell the cursor to run the query
            c.execute(statement)

            #Stores the result of the query in the data variable
            data=c.fetchone()

            #If the data matches both the password and username, then the user will be taken to the error page
            if data:
                return render_template("error.html")
            else:
                #If at least the Password or Username are different from what is in the database
                if not data:
                    #Then the user's username and password will be added into the database
                    c.execute("INSERT INTO users (Username,Password) VALUES (?,?)",(userName,passWord))
                    db2.commit()
                    db2.close()
                    #Then they are taken to the login page
                    return render_template("login.html")
                
    #When a user first goes to the register page, the page is rendered with a fresh form
    elif request.method=='GET':
        return render_template('register.html',form=PingPong)


#This is the start up function that runs when I run flask app in the command line to start the development server
def startup():
    #Connects to the database
    con = sqlite3.connect('users.db')
    #Sets a cursor
    user_cursor = con.cursor()
    #Runs a query to create a table if it does not exist
    #The two data parameters that the table can handle are a text username and a text password
    user_cursor.execute("CREATE TABLE IF NOT EXISTS users(Username text, Password text)")
    #Then the changes are added to the database
    con.commit()


#This needs to be outside of the __name__ part, because Flask skips over it.
startup()
if __name__=='__main__':
    app.run()

#End of Script
