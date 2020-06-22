from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do-the-login'
    else:
        return 'show-the-login-form'


@app.route('/about')
def about():
    return 'The about page'
