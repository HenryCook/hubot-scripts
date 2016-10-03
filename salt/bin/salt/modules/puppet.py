import environment

import requests


# Runs Puppet on requested Salt Minions
def run(args, api_token):
    puppet_tgt = args.run_puppet
    body = {"client": "local", "tgt": puppet_tgt, "fun": "cmd.run", "arg": "puppet agent --test"}
    headers = {"Accept": "application/x-yaml", "X-Auth-Token": api_token}

    try:
        requests.post(environment.salt_api_endpoint, data=body, headers=headers, verify=False)
        print("Puppet has finished running on " + puppet_tgt)
    except:
        print("Unable to run Puppet on the Salt Minion")
