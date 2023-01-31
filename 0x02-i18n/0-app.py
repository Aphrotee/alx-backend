#!/usr/bin/env pythons

"""
This module provides a flask app instance
"""

from flask import (
    Flask,
    render_template
)

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def indexHtml():
    """ Creates html template """
    page_title = 'Welcome to Holberton'
    content = 'Hello world'
    return render_template('0-index.html',
                           page_title=page_title,
                           content=content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
