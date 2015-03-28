import os, sys, getpass

# needs to see if credentials exist, otherwise prompt for them
def getCredents():
	credentpath = "%s/.gitcredents" % os.getenv('HOME')
	if not os.path.exists(credentpath):
		username = raw_input("Please enter GitHub username: ")
		password = getpass.getpass("Please enter GitHub password: ")
		credents = open(credentpath, 'w')
		credents.write("%s\n%s" % (username,password))
		return (username,password)
	else:
		credents = open(credentpath, 'r')
		username = credents.readline()
		password = credents.readline()
		return (username, password)

# prepare git repo locally by creating folder and running git init (and possibly pulling)
def prepareDirectory():
	pass



# create github repo on github! return something if the repo exists already
def createRepo():
	pass

def deleteCredents():
	os.remove("%s/.gitcredents" % os.getenv('HOME'))
