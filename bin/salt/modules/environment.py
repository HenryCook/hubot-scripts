import os
import sys

# Checks to see if the required environment variables had been set
try:
    salt_api_endpoint = os.environ['SALT_API_ENDPOINT']
    salt_api_user = os.environ['SALT_API_USER']
    salt_api_password = os.environ['SALT_API_PASSWORD']
except KeyError as i:
    print("Error: The {env} environment variable has not been set").format(env=i)
    sys.exit()
