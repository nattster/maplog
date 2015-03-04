# maplog - location logger example

A quick and simple web application that 

 * provides REST API to client application on Android devices
 * display submitted locations in Google Maps

![Maplog screenshot](/img/screenshot.png?raw=true "Screenshot")

This simple web server was used as a backend for "Sensing, Location and GPS" in [Selected Topics in Mobile Software Development](https://mike.cpe.ku.ac.th/01204496/).

# install dependency & run

    pip install -r requirements.txt
	python manage.py runserver

# how to use

1. See maps

    http://localhost:8000/

2. Submit location

	http://localhost:8000/add?lat=12.7500&lng=99.4833&color=00FF00&title=Test

	Parameters:

	* lat=12.7500  -- Latitude
	* lng=99.4833 -- Longitude
	* color=00FF00 -- Marker color in RRGGBB
	* title=Test -- Tooltip for this location

