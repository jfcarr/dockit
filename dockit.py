#!/usr/bin/python3

import os
import json
import sys

class CDockerMgr:
	def __init__(self):
		full_config_path = "{0}/dockit.json".format(os.path.dirname(os.path.realpath(__file__)))
		with open(full_config_path) as json_data:
			self.configData = json.load(json_data)
			self.dockerCmd = self.configData["dockercommand"]

	def ExecuteBaseCommand(self, currentCommand):
		for childkey,childvalue in self.configData["commands"]["base"].items():
			keyCommand,keyHelp = self.GetKeyParts(childkey)
			if keyCommand == currentCommand:
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

	def GetKeyParts(self, keyValue):
		keySplit = keyValue.split("|")
		keyCommand = keySplit[0]
		if len(keySplit) == 2:
			keyHelp = keySplit[1]
		else:
			keyHelp = ""

		return keyCommand,keyHelp

	def GetHelpLine(self, keyValue):
		keyCommand,keyHelp = self.GetKeyParts(keyValue)
		if keyHelp == "":
			return "{0}".format(keyCommand)
		else:
			return "{0} ({1})".format(keyCommand, keyHelp)

	def ShowHelp(self):
		print("USAGE:")
		print("\tdockit <command>")
		print("\tor")
		print("\tdockit <container> <command>")
		print("")
		print("Valid containers and commands:")
		for childkey,childvalue in self.configData["commands"]["base"].items():
			print("\t{0}".format(self.GetHelpLine(childkey)))
		for containerKey in self.configData["commands"]["containers"]:
			print("\t{0}".format(self.GetHelpLine(containerKey)))
			for childkey,childvalue in self.configData["commands"]["containers"][containerKey].items():
				print("\t\t{0}".format(self.GetHelpLine(childkey)))
		exit(0)

myDockerMgr = CDockerMgr()

if len(sys.argv) == 2:
	myDockerMgr.ExecuteBaseCommand(sys.argv[1])
elif len(sys.argv) == 3:
	myDockerMgr.ExecuteContainerCommand(sys.argv[1], sys.argv[2])
else:
	myDockerMgr.ShowHelp()
