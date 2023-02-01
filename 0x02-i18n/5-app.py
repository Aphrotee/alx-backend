#!/usr/bin/env python3

"""
This module provides a flask app instance
"""

from flask import (
    flash,
    Flask,
    g,
    render_template,
    request
)
from flask_babel import Babel, gettext


class Config:
    """ A Config class for configuration """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """ Gets the language to be used """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Gets the user to be logged in as """
    user = request.args.get('login_as')
    if user is not None:
        return users.get(user, None)
    return None


@app.before_request
def before_request():
    user = get_user()
    g.user = user


@app.route('/', strict_slashes=False)
def indexHtml() -> str:
    """ Creates html template """
    user = g.user
    login_status = 'not_logged_in'
    if user is not None:
        login_status = 'logged_in_as'
        username = user['name']
    return render_template('5-index.html',
                           login_status=login_status,
                           username=username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
