# Find distance between two points

## Instructions

To execute the program is only needed Docker. Just clone the repo or download the code and execute the docker commands: 
```
docker-compose build
docker-compose up 
```
(inside the folder where docker files are) to install all the dependencies and execute the flask server app.

## Endpoints

- _**[GET]**_ http://localhost:5000/
- _**[GET]**_ http://localhost:5000/placeToSearchDistance

## URL Examples

- _**[GET]**_ http://localhost:5000/Mexico

  Or even putting the longitude and latitude on browser or with another program like _**Postman**_

- _**[GET]**_ http://localhost:5000/-105.983713 54.164145
- _**[GET]**_ http://localhost:5000/170.455747,-44.069583

## Logic Behind

The logic behind the app is simple, I use the api [Yandex Geocoder API ](https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html) to search for an address using its name or coordinates (longitude and latitude) to get some data about that address, then to find the distance between two points I use [Geopy library](https://pypi.org/project/geopy/) to calculate the geodesic distance between points.
Using the "ellipsoidal model of the earth to use by specifying an ellipsoid keyword argument. The default is ‘WGS-84’, which is the most globally accurate model.".
Also to make it a little bit more accurate I added some conditionals inside _**distance file**_ putting the limits of the coordinates for **Moscow Ring Road** that I found and comparing the coordinates (longitude and latitude) received to that limits.

Inside the _**api file**_ there is a part where there are some _**try and catch**_ nested, the first one is to check if the response have no result but was successful (status code 200) then enters to the next one which is the one who process data response and creates the object with the info to add it to a list and return that list.

Finally, inside _**routes file**_ we have conditionals to handle every posible response from api, catching many possible errors and processing data if is it possible, otherwise returning a message error.
