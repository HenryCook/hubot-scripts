# hubot-scripts

Various Hubot scripts

## Reason

After perusing the currently available [hubot-scripts via the official GitHub repo](https://github.com/hubot-scripts) I realised there were a few I needed that either didn't exist, or hadn't been shared publically. So I thought I'd try my hand at writing my own and share my creations.

## Scripts

### Salt

I wanted to be able to use Salt API to use `cmd.run` for remote execution on Salt minions. It currently only supports:

- Executing Puppet runs
- Pinging a Salt Minion
- Generating a Salt API token


## Usage

### `Bin`

You will need to put the `x.coffee` script inside the `scripts` Hubot directory e.g. `/opt/hubot/scripts/salt.coffee`


### `Scripts`

If the `x.coffee` script has an accompanying script you can place them inside the `bin` Hubot directory e.g. `/opt/hubot/bin/salt_api.py`


## To Do

- Create an input prompt for Salt Puppet run, as you are currently able to use wildcards without prompting to make sure you want to do this.