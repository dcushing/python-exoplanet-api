import os

from flask import Flask, jsonify, request

# note to self: namespace the api!!
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'exoplanet_api.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello', methods = ['GET','POST'])
    def home():
        if(request.method == 'GET'):
            data = 'Hello, World!'
            return jsonify({'data': data})

    # database
    from . import db
    db.init_app(app)

    # exoplanet
    from . import exoplanet
    app.register_blueprint(exoplanet.bp)

    # api
    from .api.v1 import v1
    app.register_blueprint(v1)

    return app