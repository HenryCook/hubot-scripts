import sys
import os

# Checks to see if the required environment variables had been set
try:
    elasticsearch_endpoint = os.environ['ELASTICSEARCH_ENDPOINT']
except KeyError as i:
    print("Error: The ", i, " environment variable has not been set")
    sys.exit()