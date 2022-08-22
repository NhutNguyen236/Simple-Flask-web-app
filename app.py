from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# create flask app
app = Flask(__name__)
app.secret_key = "hello world shinobi"

# greeting route
@app.route('/')
def index():
    # get flash messages
    flash("Tell me your name?")
    # render template
    return render_template('index.html')


@app.route("/hello", methods=['POST', 'GET'])
def greeter():
    flash("🥥 Hello " + str(request.form['name_input']) + " 🌴")
    return render_template('index.html')
