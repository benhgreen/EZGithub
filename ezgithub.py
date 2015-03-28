import sys

from gitFuncs import *
from localFuncs import *


def main():
	argc = len(sys.argv)
	if argc != 2:
		print "usage: github-init <reponame> <branch>"
		return
	else:
		(username, password) = getCredents()
		gitobj = getGithub(username, password)

		if gitobj is None:
			print ("Invalid GitHub credents detected. Please relaunch to enter proper credents.")
			deleteCredents()
		else:
			print "Credents valid!"

if __name__ == '__main__':
	main()