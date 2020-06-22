from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do-the-login'
    else:
        return 'show-the-login-form'


@app.route('/about')
def about():
    return 'The about page'


@app.errorhandler(404)
def page_not_found(error):
    return error
