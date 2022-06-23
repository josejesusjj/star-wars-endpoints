"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, FavoritesPeople, FavoritesPlanets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200
@app.route('/users', methods=['GET'])
def handle_users():
    users = User.query.all()
    response_body = []
    for user in users:
        response_body.append(user.serialize())


    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def handle_people():
    people = People.query.all()
    response_body = []
    for people in people:
        response_body.append(people.serialize())


    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def handle_planets():
    planets = Planets.query.all()
    response_body = []
    for planet in planets:
        response_body.append(planet.serialize())


    return jsonify(response_body), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_people_by_id(id):
    people = People.get_by_id(id)
    if people: 
        return jsonify(people.serialize()), 200
    return ({'error': 'Character not found'}), 404

@app.route('/planets/<int:id>', methods=['GET'])
def get_planet_by_id(id):
    planet = Planets.get_by_id(id)
    if planet: 
        return jsonify(planet.serialize()), 200
    return ({'error': 'Planet not found'}), 404


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
