#!/usr/bin/python3

import os
import json
import sys

class CDockerMgr:
	def __init__(self):
		with open('dockit.json') as json_data:
			self.configData = json.load(json_data)
			self.dockerCmd = self.configData["dockercommand"]

	def ExecuteBaseCommand(self, currentCommand):
		for childkey,childvalue in self.configData["commands"]["base"].items():
			if childkey == currentCommand:
				self.ExecDocker(childvalue)
		self.ShowHelp()

	def ExecuteContainerCommand(self, currentContainer, currentCommand):
		for containerKey in self.configData["commands"]["containers"]:
			if containerKey == currentContainer:
				for childkey,childvalue in self.configData["commands"]["containers"][containerKey].items():
					if childkey == currentCommand:
						self.ExecDocker(childvalue)
		self.ShowHelp()

	def ExecDocker(self, args):
		fullCmd = "{0} {1}".format(self.dockerCmd, args)
		os.system(fullCmd)
		exit(0)

	def ShowHelp(self):
		print("USAGE:")
		print("\tdockit <container> <command>")
		print("")
		print("Valid containers and commands:")
		for childkey,childvalue in self.configData["commands"]["base"].items():
			print("\t{0}".format(childkey))
		for containerKey in self.configData["commands"]["containers"]:
			print("\t{0}".format(containerKey))
			for childkey,childvalue in self.configData["commands"]["containers"][containerKey].items():
				print("\t\t{0}".format(childkey))
		exit(0)

myDockerMgr = CDockerMgr()

if len(sys.argv) == 2:
	myDockerMgr.ExecuteBaseCommand(sys.argv[1])
elif len(sys.argv) == 3:
	myDockerMgr.ExecuteContainerCommand(sys.argv[1], sys.argv[2])
else:
	myDockerMgr.ShowHelp()
