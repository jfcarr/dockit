#!/usr/bin/python3

import os
import sys

class CDockerMgr:
	dockerCmd = 'sudo docker'

	def __init__(self):
		pass

	def ExecuteBaseCommand(self, currentCommand):
		if currentCommand == 'status':
			self.ExecDocker("ps -a")
		else:
			self.ShowHelp()

	def ExecuteContainerCommand(self, currentContainer, currentCommand):
		if currentContainer == 'sql1':
			if currentCommand == 'start':
				self.ExecDocker("restart {0}".format(currentContainer))
			elif currentCommand == 'stop':
				self.ExecDocker("stop {0}".format(currentContainer))
			elif currentCommand == 'bash':
				self.ExecDocker("exec -it {0} 'bash'".format(currentContainer))
			else:
				self.ShowHelp()
		elif currentContainer == 'busybox':
			if currentCommand == 'run':
				self.ExecDocker("run -it --rm {0}".format(currentContainer))
			else:
				self.ShowHelp()
		else:
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
		print("\tstatus")
		print("\tsql1")
		print("\t\tstart")
		print("\t\tstop")
		print("\t\tbash")
		print("\tbusybox")
		print("\t\trun")
		
		exit(0)
	
myDockerMgr = CDockerMgr()

if len(sys.argv) == 2:
	myDockerMgr.ExecuteBaseCommand(sys.argv[1])
elif len(sys.argv) == 3:
	myDockerMgr.ExecuteContainerCommand(sys.argv[1], sys.argv[2])
else:
	myDockerMgr.ShowHelp()
