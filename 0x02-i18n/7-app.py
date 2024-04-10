#!/usr/bin/env python3
"""
Module - app
"""
import pytz
from datetime import datetime
from flask_babel import Babel, format_datetime
from flask import Flask, render_template, request, g

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
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


@babel.localeselector
def get_locale() -> str:
    """
    get locale of user and guess language
    """
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    gets timezone
    """
    try:
        if request.args.get('timezone'):
            return pytz.timezone(request.args.get('timezone')).zone
        if g.user and g.user.get('timezone'):
            return pytz.timezone(g.user['timezone']).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return 'UTC'


@app.route('/')
def index() -> str:
    """
    index
    """
    curr_time = format_datetime(datetime.now())
    return render_template('7-index.html', curr_time=curr_time)


if __name__ == "__main__":
    app.run(debug=True)
