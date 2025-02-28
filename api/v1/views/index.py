#!/usr/bin/python3
""" Index file """

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


@app_views.route('/status', methods=['GET'])
def get_status():
    """ Return status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ Return stats"""
    classes = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),

    }
    return jsonify(classes)
