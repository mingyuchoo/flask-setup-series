from flask import Flask, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    username = request.cookies.get('username')
    app.logger.debug('index()')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    app.logger.debug('login()')
    if request.method == 'POST':
        return 'do-the-login'
    else:
        return 'show-the-login-form'


@app.route('/about')
def about():
    app.logger.deug('about()')
    return 'The about page'


@app.route('/me')
def me_api():
    app.logger.debug('me_api()')
    return {
        "username": "Patrick",
        "theme": "dark",
        "image": "http:image.com/profile/patrick"
    }


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug('page_not-found(error)')
    return error
