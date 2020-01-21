from flask import Blueprint
from flask_restplus import Api, Resource
v1 = Blueprint('v1', __name__)
api = Api(v1)

ns_exoplanet=api.namespace('exoplanets', description='Exoplanet operations')

@ns_exoplanet.route("/")
class ExoplanetNamespace(Resource):
    def get(self):
        return { "hello": "world"}