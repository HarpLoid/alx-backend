#!/usr/bin/env python3
"""
Module - app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale() -> str:
    """
    get locale of user and guess language
    """
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    index of app
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
