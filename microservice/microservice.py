import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/observations', methods=['GET'])
def get_observations():
    park_name = request.args.get('park_name')
    if not park_name:
        return 'Error: Park name not specified.'

    url = f'https://api.inaturalist.org/v1/observations'
    params = {
        'q': park_name,
        'order_by': 'observed_on',
        'has_photos': True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        observations = response.json()['results']
        return {'observations': observations}
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run()
