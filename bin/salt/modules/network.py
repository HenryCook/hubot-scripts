import environment

import requests


# Pings a Salt Minion from Salt Master
def ping_minion(args, api_token):
    ping_tgt = args.ping
    body = {"client": "local", "tgt": ping_tgt, "fun": "test.ping"}
    headers = {"Accept": "application/x-yaml", "X-Auth-Token": api_token}

    try:
        requests.post(environment.salt_api_endpoint, data=body, headers=headers, verify=False)
        print("The Salt Master was able to successfully ping " + ping_tgt)
    except:
        print("The Salt Master is unable to ping the Salt Minion")
