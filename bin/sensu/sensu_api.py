#!/usr/bin/env python
import argparse
import sys

import modules.system as system
import modules.clients as clients


# Arguments for script
def parse_args():
    parser = argparse.ArgumentParser(description='Salt API tool')
    parser.add_argument('-i', '--info', action='store_true', help='Display status information')
    parser.add_argument('-c', '--clients-info', action='store', help='Display Sensu client details')
    parser.add_argument('-r', '--clients-remove', action='store', help='Remove client from Sensu')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.info:
        system.info()
    elif args.clients_info:
        clients.clients_info(args)
    elif args.clients_remove:
        clients.clients_remove(args)
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()
