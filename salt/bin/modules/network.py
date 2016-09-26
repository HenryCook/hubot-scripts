import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Pings a Salt Minion from Salt Master
def ping_minion(args, api_token):
    ping_tgt = args.ping
    body = {"client": "local", "tgt": ping_tgt, "fun": "test.ping"}
    headers = {"Accept": "application/x-yaml", "X-Auth-Token": api_token}

    try:
        ping_minion = requests.post(salt_api_endpoint, data=body, headers=headers, verify=False)
        response = ping_minion.content
        print("The Salt Master was able to successfully ping " + ping_tgt)
    except:
        print("The Salt Master is unable to ping the Salt Minion")
