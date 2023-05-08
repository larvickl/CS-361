from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/observations', methods=['GET'])
def get_observations():
    park_name = request.args.get('park_name')
    if not park_name:
        return jsonify({'error': 'No park name provided.'}), 400

    url = 'https://api.inaturalist.org/v1/observations'
    params = {'q': park_name, 'order_by': 'observed_on'}
    response = requests.get(url, params=params)
    observations = response.json()['results']

    filtered_observations = [obs for obs in observations if
                             obs.get('observation_photos_count', 0) > 0 and obs.get('taxon') and obs['taxon'].get(
                                 'common_name')]

    data = [{'The Common Name': obs['taxon']['common_name'], 'The URI of the Observation': obs['uri'],
                       'Observed Date': obs['observed_on'],
                       'A Photo of the Observation': obs['photos'][0]['medium_url']} for obs in filtered_observations]

    return jsonify(data)

if __name__ == '__main__':
    app.run()
