import environment

import requests
import json


# Runs Puppet on requested Salt Minions
def clients_info(args):
    clients_info_tgt = args.clients_info
    try:
        response = requests.get("http://" + environment.sensu_endpoint + "/clients/" + clients_info_tgt)
        parsed = json.dumps(response.json(), indent=2)
        print(parsed)
    except:
        print(parsed)


def clients_remove(args):
    clients_remove_tgt = args.clients_remove
    try:
        requests.delete("http://" + environment.sensu_endpoint + "/clients/" + clients_remove_tgt)
        print("Succesfully removed the client from Sensu '%s'" % clients_remove_tgt)
    except:
        print("Unable to remove the client from Sensu '%s'" % clients_remove_tgt)
