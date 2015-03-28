import os, sys, getpass

# needs to see if credentials exist, otherwise prompt for them
def getCredents():
	credentpath = "%s/.gitcredents" % os.getenv('HOME')
	if not os.path.exists(credentpath):
		username = raw_input("Please enter GitHub username: ")
		password = getpass.getpass("Please enter GitHub password: ")
		credents = open(credentpath, 'w')
		credents.write("%s\n%s" % (username,password))
	else:
		credents = open(credentpath, 'r')
		username = credents.readline()
		password = credents.readline()
	username = username.replace('\n', '')
	password = password.replace('\n', '')
	return (username, password)

def deleteCredents():
	os.remove("%s/.gitcredents" % os.getenv('HOME'))

def folderExists(name):
	return (os.path.exists(name) and os.path.isdir(name))
