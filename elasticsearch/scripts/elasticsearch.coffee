# Description:
#   Interacts with Elasticsearch
#
# Commands:
#   hubot elasticsearch list indices - Lists all indices in ElasticSearch Cluster.
#   hubot elasticsearch remove index <host> - Removes index from Elasticsearch Cluster.
#
# Configuration:
#   ELASTICSEARCH_ENDPOINT - The endpoint for Salt's REST API
#
# Author:
#   HenryCook <henry@havingatinker.uk>

{spawn, exec}  = require 'child_process'
module.exports = (robot) ->

  robot.respond /elasticsearch remove index ([^ ]+)\s*(\w*)/i, (msg) ->
    c = "/opt/hubot/bin/elasticsearch/elasticsearch.py "+ msg.match[1]
    exec c, (err, stdout, stderr) ->
      msg.send stdout
