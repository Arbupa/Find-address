from flask import Blueprint
import requests
from api.address import Address
from api.api import search_address
from api.distance import find_distance

api_route = Blueprint('api_route', __name__)


# index route with examples to use the app
@api_route.route('/', methods=['GET'])
def index():
    return {
        'title': 'Add your search on the url.Examples:',
        'example1': 'http://localhost:5000/Moscow',
        'example2': 'http://localhost:5000/-53.373061 -8.626851'
    }


# route to search directly on the browser
@api_route.route('/<address>', methods=['GET'])
def calculate_address(address):
    # if an object response founded,
    if len(search_address(address)) != 0:
        location_api = search_address(address)
        # if the object address object not exist then return error message.
        if location_api == ["There was an error. Send the request again."]:
            print("There was an error. Send the request again.")
            return "There was an error. Send the request again."
        # store the distance founded from the coordinates given
        distance_km = find_distance(location_api[0].lon, location_api[0].lat)
        # if to check if the distance is inside the MKAD
        if distance_km == "Inside":
            print("The distance is inside Moscow Ring Road")
            return "The distance is inside Moscow Ring Road"
        print(
            f"The distance from Moscow Ring Road to {location_api[0].name} is : {distance_km} km")
        return f"The distance from Moscow Ring Road to {location_api[0].name} is : {distance_km} km"

    message_error = {
        'url': 'Error from http://localhost:5000/' + address,
        'message': 'Sorry, your location was not found'
    }
    print(message_error)
    # error message if a bad request its done.
    return message_error
