
![2023-05-07](https://user-images.githubusercontent.com/107569872/236730780-bf915a69-70a9-4dba-85a7-75a472ee8a6e.png)

How to Request Data:

url = 'https://api.inaturalist.org/v1/observations'

params = {'q': park_name, 'order_by': 'observed_on'}

response = requests.get(url, params=params)

Query Params = park_name

If there is no parameter entered for park_name, returns: 
{
  "error": "Missing park_name parameter"
}

The parameter park_name is case-sensitive, as it relies on the iNaturalist API.

How to Receive Data: The data will be returned as a collection of 'Observations'.  An example is below.
From running the code in a terminal, (after running pip install requests), use the command python microservice.py.  
The microservice can then be called by sending an HTTP request.

data :
[
  {name: example_name, uri: example_uri, observed_date: example_observed_date, photo:
  example_photo.jpg},
  {name: example_name, uri: example_uri, observed_date: example_observed_date, photo:
  example_photo.jpg},
  {name: example_name, uri: example_uri, observed_date: example_observed_date, photo:
  example_photo.jpg},
  {name: example_name, uri: example_uri, observed_date: example_observed_date, photo:
  example_photo.jpg},
  {name: example_name, uri: example_uri, observed_date: example_observed_date, photo:
  example_photo.jpg}
]
