# CrocCatGin - Rayat Roy, Michelle Lo, Tami Takada
# SoftDev
# K14 - Form and Function
# 2021-10-14

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    return render_template(
        'response.html',
        username = request.args['username'],
        method = request.method
    ) #response to a form submission



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
