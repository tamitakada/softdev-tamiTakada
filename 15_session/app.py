# CrocCatGin - Rayat Roy, Michelle Lo, Tami Takada
# SoftDev
# K15 - Sessions Greetings
# 2021-10-18

# Questions: what does the POST method do?

from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
print(app.secret_key)

@app.route('/', methods=['GET', 'POST'])
def disp_loginpage():
    """Renders either the login or the response page based on whether the user is logged in or not."""
    if request.method == 'POST': # triggered when the user clicks the log out button
        session.pop('username')
        return render_template('login.html')
    else:
        try:
            #renders response using response template
            return render_template(
                'response.html',
                result = 'true',
                username = session['username']
            )
        except:
            return render_template( 'login.html' )

@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    """Renders the response from the login page based on the user input."""
    username = request.args['username']
    password = request.args['password']
    result = validate_login(username, password) #determines if username and/or password is correct

    if result == 'true':
        session['username'] = username

    #renders response using response template
    return render_template(
        'response.html',
        result = result,
        username = request.args['username']
    )

def validate_login(username, password):
    """Method to validate user input """
    if username == 'CrocCatGin':
        if password == 'password':
            return 'true'
        else:
            return 'bad password'
    else:
        return 'bad username'

if __name__ == '__main__': #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
