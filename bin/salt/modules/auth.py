import environment

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


# Generates Salt API token and returns it
def get_token(args):
    if args.disable_ssl_verification is True:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    else:
        pass

    request_body_data = {"username": environment.salt_api_user, "password": environment.salt_api_password, "eauth": "pam"}

    try:
        request_token = requests.post(environment.salt_api_endpoint + "/login", data=request_body_data, verify=False)
        api_token = request_token.json()['return'][0]['token']
        return api_token
    except:
        return False
