from flask import Flask, render_template
from userData import data

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def HomePage():
	return render_template('index.html')

@app.route('/users/<username>')
def userPage(username):
	return "Hello {username}!"

@app.route('/about/')
def AboutPage():
	return "HelloWorld!"

#comment
