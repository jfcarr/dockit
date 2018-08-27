#!/usr/bin/python3

import json

with open('dockit.json') as json_data:
	configData = json.load(json_data)

	print("Docker command is '{0}'\n".format(configData["dockercommand"]))
	
	print("Base commands:\n")
	for childkey,childvalue in configData["commands"]["base"].items():
		print(" {0} -> {1}".format(childkey,childvalue))
	print("")
	
	print("Container commands:\n")
	for containerKey in configData["commands"]["containers"]:
		for childkey,childvalue in configData["commands"]["containers"][containerKey].items():
			print(" {0}.{1} -> {2}".format(containerKey,childkey,childvalue))
		print("")
