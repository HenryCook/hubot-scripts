#!/usr/bin/env python
import argparse
import sys

import modules.auth as auth
import modules.network as network
import modules.puppet as puppet


# Arguments for script
def parse_args():
    parser = argparse.ArgumentParser(description='Salt API tool')
    parser.add_argument('-p', '--ping', action='store', help='Ping a Salt Minion from the Salt Master')
    parser.add_argument('-r', '--run-puppet', action='store', help='Run Puppet on a Salt Minion')
    parser.add_argument('-d', '--disable-ssl-verification', action='store_true', help='Disables SSL verification')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    api_token = auth.get_token(args)
    if api_token:
        pass
    else:
        print('Failed to get auth token for Salt API')
        sys.exit(2)

    if args.run_puppet:
        puppet.run(args, api_token)
    elif args.ping:
        network.ping_minion(args, api_token)
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()
