from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/observations', methods=['GET'])
def get_observations():
    park_name = request.args.get('park_name')

    if not park_name:
        return jsonify({'error': 'Missing park_name parameter'}), 400

    observations = get_park_observations(park_name)

    if observations is not None:
        filtered_observations = filter_observations(observations)
        return jsonify({'data': filtered_observations})
    else:
        return jsonify({'error': 'Failed to retrieve observations'}), 500

def get_park_observations(park_name):
    base_url = "https://api.inaturalist.org/v1/observations"
    params = {
        "q": park_name,
        "order_by": "observed_on",
        "has_photos": True
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None

def filter_observations(observations):
    filtered_data = []
    counter = 0
    for observation in observations["results"]:
        if counter == 10:
            break
        taxon_name = observation["taxon"]["preferred_common_name"]
        uri = observation["uri"]
        observed_on = observation["observed_on"]
        photo_url = observation["photos"][0]["url"] if len(observation["photos"]) > 0 else None

        filtered_observation = {
            "name": taxon_name,
            "uri": uri,
            "observed_date": observed_on,
            "photo": photo_url
        }
        filtered_data.append(filtered_observation)
        counter += 1

    return filtered_data


if __name__ == '__main__':
    app.run(debug=True, port=5000)

