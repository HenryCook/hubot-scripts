#!/usr/bin/env python
import os
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import argparse

# Checks to see if the required environment variables had been set
try:
    salt_api_endpoint = os.environ['SALT_API_ENDPOINT']
    salt_api_user = os.environ['SALT_API_USER']
    salt_api_password = os.environ['SALT_API_PASSWORD']
except KeyError as i:
    print "Error: The ", i, " environment variable has not been set"
    sys.exit()


# Arguments for script
def parse_args():
    parser = argparse.ArgumentParser(description='Salt API tool')
    parser.add_argument('-p', '--ping', action='store', help='Ping a Salt Minion from the Salt Master')
    parser.add_argument('-r', '--run_puppet', action='store', help='Run Puppet on a Salt Minion')
    parser.add_argument('-t', '--token', action='store_true', help='Print the requested Salt API auth token')
    parser.add_argument('-d', '--disable-ssl-verification', action='store_true', help='Disables SSL verification')
    args = parser.parse_args()
    return args


# Generates Salt API token and returns it
def auth_salt_api():
    if parse_args().disable_ssl_verification is True:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    else:
        pass

    request_body_data = {"username": {salt_api_user}, "password": {salt_api_password}, "eauth": "pam"}

    try:
        request_token = requests.post(salt_api_endpoint + "/login", data=request_body_data, verify=False)
        api_token = request_token.json()['return'][0]['token']
        return api_token
    except:
        print("Unable to retrieve token")


# Pings a Salt Minion from Salt Master
def ping_minion():
    ping_tgt = parse_args().ping
    api_token = auth_salt_api()
    body = {"client": "local", "tgt": ping_tgt, "fun": "test.ping"}
    headers = {"Accept": "application/x-yaml", "X-Auth-Token": api_token}

    try:
        ping_minion = requests.post(salt_api_endpoint, data=body, headers=headers, verify=False)
        response = ping_minion.content
        print("The Salt Master was able to successfully ping " + ping_tgt)
    except:
        print("The Salt Master is unable to ping the Salt Minion")


# Runs Puppet on requested Salt Minions
def run_puppet():
    puppet_tgt = parse_args().run_puppet
    api_token = auth_salt_api()
    body = {"client": "local", "tgt": puppet_tgt, "fun": "cmd.run", "arg": "puppet agent --test"}
    headers = {"Accept": "application/x-yaml", "X-Auth-Token": api_token}

    try:
        print("Running Puppet on" + puppet_tgt)
        puppet_minion = requests.post(salt_api_endpoint, data=body, headers=headers, verify=False)
        response = puppet_minion.content
        print("Puppet has finished running on " + puppet_tgt)
    except:
        print("Unable to run Puppet on the Salt Minion")


def main():
    args = parse_args()

    if args.run_puppet:
        run_puppet()
    elif args.ping:
        ping_minion()
    elif args.token:
        print("Temporary Salt API auth token: " + auth_salt_api())
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()