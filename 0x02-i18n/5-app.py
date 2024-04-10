#!/usr/bin/env python3
"""
Module - app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEF_LOCALE = "en"
    BABEL_DEF_TIMEZONE = "UTC"

app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    get locale of user and guess language
    """
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    index
    """
    return render_template('5-index.html')

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    gets user logged in
    """
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None

@app.before_request
def before_request():
    """
    finds a user from get request
    """
    g.user = get_user()

if __name__ == "__main__":
    app.run(debug=True)
