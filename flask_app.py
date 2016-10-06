from flask import Flask
from flask import Response
from flask import request
from flask import render_template

flask_app = Flask('flaskapp', static_folder='public')
flask_app.add_url_rule(
	'/', 'root', lambda: flask_app.send_static_file('index.html'))


@flask_app.route('/<path:path>')
def get_static_file(path):
	return flask_app.send_static_file(path)

app = flask_app.wsgi_app
