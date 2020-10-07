import json
import os
from urllib.request import urljoin
import requests

def call_api():
    create_url()

def create_url():
    #create url for the specific city to call the API
    API_KEY = os.environ["WORLD_AIR_API"]
    token_address = "?token=" + API_KEY 
    base_url = "https://api.waqi.info/feed"
    city_name = "seoul"
    city_url = '{}/{}/{}'.format(base_url, city_name, token_address)
    response = requests.get(city_url)
    # create a formatted string of the JSON object
    formatted_response = json.dumps(response.json(), sort_keys=True, indent=4)
    # write file
    outfile_name = "airquality_" + city_name
    with open(outfile_name, 'w') as outfile:
        outfile.write(formatted_response)

if __name__ == '__main__':
    call_api()

