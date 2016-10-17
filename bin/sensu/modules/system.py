import environment

import requests
import json


# Runs Puppet on requested Salt Minions
def info():
    endpoint = "{es}/info".format(es=environment.sensu_endpoint)
    try:
        response = requests.get(endpoint)
        parsed = response.json()
        pretty = json.dumps(parsed, indent=2)
        print(pretty)
    except:
        print(pretty)
