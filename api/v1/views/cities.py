#!/usr/bin/python3
"""new view for City objects that handle all default RESTFul  API"""
from api.v1.views import app_views
from models import storage
from models.city import City
from flask import abort, jsonify, request


@app_views.route('/cities/<city_id>', methods=['GET'])
def listallcities(city_id=None):
    """Retrieves a City object"""
    c = storage.get("City", city_id)
    if c is None:
        abort(404)
    else:
        return (jsonify(c.to_dict()), 200)

@app_views.route('/cities/<city_id>', methods=['DELETE'])
def deletecity(city_id=None):
    """Deletes a City object"""
    c = storage.get("City", city_id)
    if c is None:
        abort(404)
    else:
        storage.delete(ct)
        storage.save()
        return (jsonify({}), 200)

@app_views.route('/states/<state_id>/cities', methods=['POST'])
def createcity():
    """Creates a City"""
    s = storage.get("State", state_id)
    if s is None:
        abort(404)
    c = storage.request.get_json()
    if c == None:
        return (400, "Not a JSON")
    elif "name" not in  c.keys():
        return (400, "Missing name")
    else:
        instance = City(**data)
        instance.state_id = state.id
        instance.save()
        return (jsonify(instance.to_dict()), 201)

@app_views.route('/cities/<city_id>', method=['PUT'])
def updatecity(city_id=None):
    """Updates a City object"""
    ct = storage.get("City", city_id)
    if ct is None:
        abort(404)
    c = request.get_json()
    if c is None:
        abort(400, "Not a JSON")
    else:
        for key, value in c.items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(ct, key, value)
        storage.save()
        return (jsonify(ct.to_dict()), 200)
