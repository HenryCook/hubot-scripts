from elasticsearch import Elasticsearch

import environment


def es(args):
    # Creates the connection with Elasticsearch
    conn = Elasticsearch(environment.elasticsearch_endpoint)

    return conn
