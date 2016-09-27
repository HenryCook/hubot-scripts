import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import environment


# Runs Puppet on requested Salt Minions
def run(args, api_token):
    puppet_tgt = args.run_puppet
    body = {"client": "local", "tgt": puppet_tgt, "fun": "cmd.run", "arg": "puppet agent --test"}
    headers = {"Accept": "application/x-yaml", "X-Auth-Token": api_token}

    print("Attempting a Puppet run on " + puppet_tgt)

    try:
        requests.post(environment.salt_api_endpoint, data=body, headers=headers, verify=False)
        print("Puppet has finished running on " + puppet_tgt)
    except:
        print("Unable to run Puppet on the Salt Minion")