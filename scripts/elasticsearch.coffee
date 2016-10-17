# Description:
#   Interacts with Elasticsearch
#
# Commands:
#   hubot elasticsearch list indices - Lists all indices in ElasticSearch Cluster.
#   hubot elasticsearch remove index <host> - Removes index from Elasticsearch Cluster.
#
# Configuration:
#   ELASTICSEARCH_ENDPOINT - The endpoint for Salt's REST API e.g. http://elastic.search.com:80/ 
#
# Author:
#   HenryCook <henry@havingatinker.uk>

{spawn, exec}  = require 'child_process'
module.exports = (robot) ->

 robot.respond /elasticsearch list indices/i, (msg) ->
    c = "/opt/hubot/bin/elasticsearch/es_tool.py --list-all-indices"
    exec c, (err, stdout, stderr) ->
      msg.send stdout
      msg.send stderr
      msg.send err

  robot.respond /elasticsearch remove index ([^ ]+)\s*(\w*)/i, (msg) ->
    c = "/opt/hubot/bin/elasticsearch/es_tool.py --delete-index "+ msg.match[1]
    exec c, (err, stdout, stderr) ->
      msg.send stdout
      msg.send stderr
      msg.send err