# CrocCatGin - Rayat Roy, Michelle Lo, Tami Takada
# SoftDev
# K15 - Sessions Greetings
# 2021-10-18

# Questions: what does the POST method do?

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def disp_loginpage():
    """Returns the login page using the login.html template (http://127.0.0.1:5000/)"""
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    if request.args['username'] == 'CrocCatGin':
        if request.args['password'] == 'password':
            return render_template(
                'response.html',
                result = 'true',
                username = request.args['username'] #request.args returns the value for the username key (that is, the username).
            )
        else:
            return render_template(
                'response.html',
                result = 'bad password',
                username = request.args['username'] #request.args returns the value for the username key (that is, the username).
            )
    else:
        return render_template(
            'response.html',
            result = 'bad username',
            username = request.args['username'] #request.args returns the value for the username key (that is, the username).
        )


    return render_template(
        'response.html',
        username = request.args['username'], #request.args returns the value for the username key (that is, the username).
        method = request.method #Uses the GET method to display the form.
    ) #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
