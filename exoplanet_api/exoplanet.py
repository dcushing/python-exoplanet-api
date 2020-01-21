import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from exoplanet_api.db import get_db

bp = Blueprint('exoplanet', __name__, url_prefix='/exoplanet')

@bp.route('/random', methods=['GET'])
def random():
	# get a random row from the exoplanet table and return it
	db = get_db()

	# TODO: replace this with actual exoplanet data
	return jsonify({'data': 'Filler data for now'})
