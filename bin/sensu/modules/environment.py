import os
import sys

# Checks to see if the required environment variables had been set
try:
    sensu_endpoint = os.environ['SENSU_ENDPOINT']
except KeyError as i:
    print("Error: The ", i, " environment variable has not been set")
    sys.exit()
