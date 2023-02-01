#!/usr/bin/env python3

"""
This module provides a flask app instance
"""

from flask import (
    Flask,
    g,
    render_template,
    request
)
from flask_babel import Babel


class Config:
    """ A Config class for configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Gets the language to be used """
    locale = request.args.get('locale')
    if locale in app.config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def indexHtml() -> str:
    """ Creates html template """
    page_title = 'Welcome to Holberton'
    content = 'Hello world'
    return render_template('4-index.html',
                           home_title=page_title,
                           home_header=content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
