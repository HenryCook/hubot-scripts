import environment

import requests
import json


# Runs Puppet on requested Salt Minions
def info():
    try:
        response = requests.get("http://" + environment.sensu_endpoint + "/info")
        parsed = json.dumps(response.json(), indent=2)
        print(parsed)
    except:
        print(parsed)
