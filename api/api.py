import requests
from geopy.units import radians
# I've changed this line
from .address import Address


# function to search the given address using the api
def search_address(address: str) -> list:
    arr = []
    parameters = {
        "apikey": "8ef38655-abbc-4679-9073-4e4f89d1773f",
        "format": "json",
        "lang": "en_US",
        "geocode": address,
        "results": 1
    }
    # to check if the result exists (this is to try to catch an empty object response)
    try:
        response = requests.get(
            "https://geocode-maps.yandex.ru/1.x/?", params=parameters)
        data = response.json()
        print("lo que quiero ver es: ", data.get("resoponse").get(
            "GeoObjectCollection").get("featureMember"))
    # if the object was not empty, then:
    except:
        try:
            # Here I used a for loop (in case we have more than 1 address response, but
            # for now we only have 1 result).
            # iterate over the json data response
            for i in (data.get('response').get('GeoObjectCollection').get(
                    'featureMember')):
                # storing the name of each result
                name = (i.get('GeoObject').get('metaDataProperty').get(
                    'GeocoderMetaData').get('text'))
                # storing coordinates
                coord = (i.get('GeoObject').get('Point').get('pos'))
                coord2 = coord.split(" ")
                # store longitude and latitude
                lon = coord2[0]
                lat = coord2[1]
                # create the address object to store the info and add it to array.
                address_object = Address(name, lat, lon)
                arr.append(address_object)
            # return the list of address objects.
            return arr
        # if there was an error return a message error.
        except:
            print(["There was an error. Send the request again."])
            return ["There was an error. Send the request again."]

    return arr
