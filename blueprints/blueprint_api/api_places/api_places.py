from flask import Blueprint, request, jsonify
from run import PATH_API, COUNTRIES, STATES, CITIES

api_places = Blueprint("api_places", __name__)


@api_places.route("/countries", methods=['GET'])
def getCountries():
    if (request.method == 'GET'):
        res = {
            "countries": COUNTRIES
        }

    return jsonify(res)


@api_places.route("/<country>/states", methods=['GET'])
def getStatesFromCountry(country):
    if (request.method == 'GET'):
        if country in STATES:
            res = {
                "country": country,
                "states": STATES[country]
            }
        else:
            res = {
                "country": country,
                "states": []
            }

    return jsonify(res)


@api_places.route("/<country>/<state>/cities", methods=['GET'])
def getCitiesFromState(country, state):
    if (request.method == 'GET'):
        if state in CITIES:
            res = {
                "country": country,
                "state": state,
                "cities": CITIES[state]
            }
        else:
            res = {
                "country": country,
                "state": state,
                "cities": []
            }

    return jsonify(res)
