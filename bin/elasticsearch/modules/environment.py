import os
import sys


# Checks to see if the required environment variables had been set
try:
    elasticsearch_endpoint = os.environ['ELASTICSEARCH_ENDPOINT']
except KeyError as i:
    print("Error: The {env} environment variable has not been set").format(env=i)
    sys.exit()
