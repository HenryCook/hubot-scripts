#!/usr/bin/env python
import argparse
import sys

import modules.connection as connection
import modules.environment as environment
import modules.indices as indices


# Arguments for script
def parse_args():
    parser = argparse.ArgumentParser(description='Elasticsearch Tool')
    parser.add_argument('-l', '--list-all-indices', action='store_true', help='Lists all indices from Elasticsearch cluster')
    parser.add_argument('-d', '--delete-index', action='store', help='Remove index from Elasticsearch cluster')
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

    if args.list_all_indices:
        print("Attempting to list all indices in the '{endpoint}' cluster").format(endpoint = environment.elasticsearch_endpoint)
        indices.list_all(conn)
    elif args.delete_index:
        print("Attempting to remove the index '{delete}' from the '{endpoint}' cluster").format(delete=args.delete_index, endpoint = environment.elasticsearch_endpoint)
        indices.delete(args, conn)
    else:
        sys.exit()
    pass


if __name__ == "__main__":
    main()
