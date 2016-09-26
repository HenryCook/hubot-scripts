#!/usr/bin/env python
import os
import sys
import requests
import modules.auth as auth
import modules.network as network
import module.puppet as puppet


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
    parser.add_argument('-d', '--disable-ssl-verification', action='store_true', help='Disables SSL verification')
    args = parser.parse_args()
    return args
        


def main():
    args = parse_args()
    api_token = auth.get_token()
    if api_token:
        pass
    else:
        print('Failed to get auth token for Salt API')
        sys.exit(2)

    if args.run_puppet:
        puppet.run(args, api_token)
    elif args.ping:
        ping_minion(args, api_token)
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()