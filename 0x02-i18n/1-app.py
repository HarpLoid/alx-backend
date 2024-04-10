#!/usr/bin/env python3
"""
Module - app
"""
from flask import Flask, render_template
from flask_babel import Babel


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


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
