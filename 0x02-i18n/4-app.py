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
    return render_template('4-index.html',get_locale=get_locale,
                           home_title=_('home_title'),
                           home_header=_('home_header'))



if __name__ == "__main__":
    app.run(debug=True)
