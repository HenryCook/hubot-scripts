# Description:
#   Interacts with Sensu API
#
# Commands:
#   hubot sensu info - Returns some status information around Sensu.
#
# Configuration:
#   SENSU_ENDPOINT - The endpoint for Sensu's REST API e.g. http://sensu.ops.forward3d.com:4567 (notice the trailing '/')
#
# Author:
#   HenryCook <henry@havingatinker.uk>

{spawn, exec}  = require 'child_process'
module.exports = (robot) ->
  robot.respond /sensu info/i, (msg) ->
    c = "/opt/hubot/bin/sensu/sensu_api.py --info"
    exec c, (err, stdout, stderr) ->
      msg.send stdout
      msg.send stderr
      msg.send err
  
  robot.respond /sensu clients info ([^ ]+)\s*(\w*)/i, (msg) ->
      c = "/opt/hubot/bin/sensu/sensu_api.py --clients-info "+ msg.match[1]
      exec c, (err, stdout, stderr) ->
        msg.send stdout
        msg.send stderr
        msg.send err

  robot.respond /sensu clients remove ([^ ]+)\s*(\w*)/i, (msg) ->
      c = "/opt/hubot/bin/sensu/sensu_api.py --clients_remove "+ msg.match[1]
      exec c, (err, stdout, stderr) ->
        msg.send stdout
        msg.send stderr
        msg.send err