# hubot-scripts

Various Hubot scripts

## Reason

After perusing the currently available [hubot-scripts via the official GitHub repo](https://github.com/hubot-scripts) I realised there were a few I needed that either didn't exist, or hadn't been shared publically. So I thought I'd try my hand at writing my own and share my creations.



## Scripts

### Salt

I wanted to be able to use Salt API to use `cmd.run` for remote execution on Salt minions. 

	$ ./salt_api.py --help

	usage: salt_api.py [-h] [-p PING] [-r RUN_PUPPET] [-d]

	Salt API tool

	optional arguments:
	  -h, --help            show this help message and exit
	  -p PING, --ping PING  Ping a Salt Minion from the Salt Master
	  -r RUN_PUPPET, --run_puppet RUN_PUPPET
	                        Run Puppet on a Salt Minion
	  -d, --disable-ssl-verification
	                        Disables SSL verification	


### Elasticsearch

	$ ./es_tool.py --help

	usage: es_tool.py [-h] [-l] [-d DELETE_INDEX]

	Elasticsearch Tool

	optional arguments:
	  -h, --help            show this help message and exit
	  -l, --list-all-indices
	                        Lists all indices from Elasticsearch cluster
	  -d DELETE_INDEX, --delete-index DELETE_INDEX
	                        Remove index from Elasticsearch cluster


## Usage

### Structure

For portability and as a way of sectioning off your various scripts/modules in your Hubot's `bin` directory, it's worth creating directories for each script/module and then reference them from your `x.coffee` script. Here's an example of how your Hubot's parent directory could look like.

```
+-- README.md
+-- external-scripts.json
+-- node_modules
+-- package.json
+-- procfile
+-- requirements.txt
+-- bin
│   +-- elasticsearch
│   │   +-- es_tool.py
│   │   +-- modules
│   │   │   +-- __init__.py
│   │   │   +-- connection.py
│   │   │   +-- environment.py
│   │   │   \-- indices.py
│   │   \-- requirements.txt
│   \-- salt
│       +-- modules
│       │   +-- __init__.py
│       │   +-- auth.py
│       │   +-- environment.py
│       │   +-- network.py
│       │   \-- puppet.py
│       +-- requirements.txt
│       \-- salt_api.py
\-- scripts
    +-- elasticsearch.coffee
    \-- salt.coffee

```

In the above example, both `salt` and `elasticsearch` are separate scripts/modules.


#### Scripts

In here you'll find the `x.coffee` script, that needs to be inside the `scripts` Hubot directory e.g. `/opt/hubot/scripts/salt.coffee`.

#### Bin

If the `x.coffee` script has an accompanying script/module you can place them inside the `bin` Hubot directory e.g. `/opt/hubot/bin/salt/salt_api.py`.

### Dependencies

You can install the relevant dependencies needed for the script/module via it's `requirement.txt`

	pip install -r requirements.txt


## To Do

- Salt
	- Create an input prompt for Salt Puppet run, as you are currently able to use wildcards without prompting to make sure you want to do this.
    - Remove Salt Minion key from master
    - Remove node from Puppet Master

- Elasticsearch
    - Look into ssl warnings if you're not verifying ssl cert
    - Add option for auth, for when you require credentials

- Sensu
    - Remove client from Sensu


## Side note

I am more than happy to take PR's so please feel free to add something if you feel it's missing something.
