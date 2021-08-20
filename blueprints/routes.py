from flask import Blueprint
import requests
from api.address import Address
from api.api import search_address
from api.distance import find_distance

api_route = Blueprint('api_route', __name__)


@api_route.route('/', methods=['GET'])
def index():
    return "Add your search on the url.Examples: \n http://localhost:5000/Moscow \n or even putting longitude latitude coordinates \n http://localhost:5000/-53.373061 -8.626851"


@api_route.route('/<address>', methods=['GET'])
def calculate_address(address):

    if len(search_address(address)) != 0:
        location_api = search_address(address)
        if location_api == ["There was an error. Send the request again."]:
            return "There was an error. Send the request again."
        # aqui calcular la distancia
        distance_km = find_distance(location_api[0].lon, location_api[0].lat)

        if distance_km == "Inside":
            return "The distance is inside Moscow Ring Road"
        return f"The distance from Moscow Ring Road to {location_api[0].name} is : {distance_km} km"

    return {
        'url': 'Error from http://localhost:5000/' + address,
        'message': 'Sorry, your location was not found',
        'status': 404
    }
