#!/usr/bin/env python
import argparse
import sys

import modules.system as system


# Arguments for script
def parse_args():
    parser = argparse.ArgumentParser(description='Salt API tool')
    parser.add_argument('-i', '--info', action='store_true', help='Display status information')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.info:
        system.info()
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()
