#!/usr/bin/env python3
import json

confPath = "~/.ipfs/config"

with open(confPath, "r") as f:
	# Loads the config as J, all modifications can be done here.
	j = json.loads(f.read())

# Add the master of the cluster as Peering.
j["Peering"] = {"Peers":[{
	"Addrs": ["/ip4/51.75.127.200/udp/4001/quic"],
	"ID": "QmeSn1aFaDAtnM2ZjADu3F1LvuMsf63QGMRkd5hJjn8hZU"
}]}
# Set to dhtclient to reduce cpu usage and increase network stability.
j["Routing"] = {"Type":"dhtclient"}

with open(confPath, "w") as f:
	# Overwrite the config.
	f.write(json.dumps(j))
