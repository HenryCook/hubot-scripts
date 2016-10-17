import environment

import requests
import json


# Runs Puppet on requested Salt Minions
def clients_info(args):
    clients_tgt = args.clients_info
    try:
        response = requests.get("http://" + environment.sensu_endpoint + "/clients/" + clients_tgt)
        parsed = json.dumps(response.json(), indent=2)
        print(parsed)
    except:
        print(parsed)
