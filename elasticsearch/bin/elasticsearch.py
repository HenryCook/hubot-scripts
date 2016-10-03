#!/usr/bin/env python
import argparse
import sys

import modules.connection as connection
import modules.indices as indices


# Arguments for script
def parse_args():
    parser = argparse.ArgumentParser(description='Salt API tool')
    parser.add_argument('-d', '--delete_indices', action='store', help='Remove index from Elasticsearch cluster')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    conn = connection.es(args)
    if conn:
        pass
    else:
        print('Failed to connect to ES cluster')
        sys.exit(2)

    if args.delete_index:
        indices.delete(args, conn)
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()
