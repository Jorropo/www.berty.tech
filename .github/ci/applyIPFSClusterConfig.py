#!/usr/bin/env python3
import json
import os

dirPath = os.path.expanduser("~") + "/.ipfs-cluster/"
confPath = dirPath + "service.json"

with open(dirPath + "peerstore", "w") as f:
	# Writing peerstore
	f.write("/ip4/51.75.127.200/tcp/9096/p2p/12D3KooWFUTJ3WUsGShrkQjKHAH5zho4o8Sc5Lw1KqTc6cKDvKfL")

with open(confPath, "r") as f:
	# Loads the config as J, all modifications can be done here.
	j = json.loads(f.read())

# Change the name
j["cluster"]["peername"] = "CI Deploy"
# Set the Secret
j["cluster"]["secret"] = os.getenv("GITHUB_IPFS_CLUSTER_SECRET")
# Disable relay hop
j["cluster"]["enable_relay_hop"] = False
# Set Leave on shutdown, that will remove it from the peerset with it closes.
j["cluster"]["leave_on_shutdown"] = True
# Disable local discovery
j["cluster"]["mdns_interval"] = "0"
# Set wrong IPFS api port, this is a hacky way but there is no way to disable pinning while keeping consensus
j["api"]["ipfsproxy"]["node_multiaddress"] = "/ip4/127.0.0.1/tcp/5002"
j["ipfs_connector"]["ipfshttp"]["node_multiaddress"] = "/ip4/127.0.0.1/tcp/5002"

with open(confPath, "w") as f:
	# Overwrite the config.
	f.write(json.dumps(j))
