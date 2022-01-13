from flask import Flask

app = Flask(__name__)


@app.route('/')
def HomePage():
	return render_template('index.html')


@app.route('/about/')
def AboutPage():
	return render_template('about.html')

