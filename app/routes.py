from flask import jsonify, request
from app import app
import requests



@app.route('/')
def index():
    return jsonify({'status': 'ok'})


@app.route('/postcode_geocoder', methods=['POST'])
def postcode_geocoder():
    # Get the postcodes from the request
    postcodes = request.json['postcodes']

    # Prepare the data for the API call
    data = {
      "postcodes": postcodes
    }

    # Call the API
    response = requests.post('https://api.postcodes.io/postcodes', json=data)

    # Parsing the response from the API
    parsed_response = response.json()

    # Prepare the response
    postcodes = []
    # We only need the latitude and longitude
    for result in parsed_response['result']:
        postcode = result['result']['postcode']
        latitude = result['result']['latitude']
        longitude = result['result']['longitude']
        postcodes.append({
            'postcode': postcode,
            'lat': latitude,
            'lng': longitude
        })

    # Return the response
    return postcodes, 200


@app.route('/docs/postcode_geocoder', methods=['GET'])
def postcode_geocoder_docs():
    return jsonify({
        "description": "This endpoint takes a list of postcodes and returns their latitude and longitude.",
        "request_example": {
            "postcodes": ["OX49 5NU"]
          },
        "response_example": [{"postcode":"OX49 5NU","lat":51.655929,"lng":-1.069752}]
    })


@app.route('/sunset_sunrise', methods=['POST'])
def sunset_sunrise():
    lat = request.json['lat']
    lng = request.json['lng']
    response = requests.get(f"https://api.sunrisesunset.io/json?lat={lat}&lng={lng}&timezone=UTC&date=today")
    parsed_response = response.json()

    sunrise = parsed_response['results']['sunrise']
    sunset = parsed_response['results']['sunset']
    return jsonify({
        'sunrise': sunrise,
        'sunset': sunset
    }), 200


@app.route('/docs/sunset_sunrise', methods=['GET'])
def sunset_sunrise_docs():
    return jsonify({
        "description": "This endpoint takes a latitude and longitude and returns the sunrise and sunset times.",
        "request_example": {
            "lat": 51.655929,
            "lng": -1.069752
        },
        "response_example": {
            "sunrise": "12:12:45 PM",
            "sunset": "9:47:31 PM"
        }
    })