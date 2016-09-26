# Description:
#   Interacts with Salt minions
#
# Commands:
#   hubot salt ping <host> - Salt Master pings the Salt minion.
#   hubot salt puppet <host> - Runs Puppet on Salt minion.
#   hubot salt token - Returns a Salt API token.
#
# Configuration:
#   SALT_API_ENDPOINT - The endpoint for Salt's REST API
#   SALT_API_USER - Salt API user
#   SALT_API_PASSWORD - Salt API password
#
# Notes:
#   Salt REST API needs to be up and running
#   <https://docs.saltstack.com/en/latest/ref/netapi/all/salt.netapi.rest_cherrypy.html>
#
# Author:
#   HenryCook <henry@havingatinker.uk>

{spawn, exec}  = require 'child_process'
module.exports = (robot) ->
  robot.respond /salt ping ([^ ]+)\s*(\w*)/i, (msg) ->
    c = "/opt/hubot/bin/salt_api.py --ping "+ msg.match[1]
    exec c, (err, stdout, stderr) ->
      msg.send stdout

  robot.respond /salt puppet ([^ ]+)\s*(\w*)/i, (msg) ->
    c = "/opt/hubot/bin/salt_api.py --run_puppet "+ msg.match[1]
    exec c, (err, stdout, stderr) ->
      msg.send stdout

  robot.respond /salt token/, (msg) ->
    c = "/opt/hubot/bin/salt_api.py --token"
    exec c, (err, stdout, stderr) ->
      msg.send stdout