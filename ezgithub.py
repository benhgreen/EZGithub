import sys, os

from gitfuncs import *
from localfuncs import *


def main(argv):
	argc = len(argv)

	if argc != 2:
		print "usage: github-init <reponame> <branch>"
		return
	else:
		(username, password) = getCredents()
		while getGithub(username, password) is None:
			print ("Invalid GitHub credents detected.\n")
			deleteCredents()
			(username,password) = getCredents()
		
		print "Credents valid!"
		
		repo_name = argv[1]
		gitobj = Github(username,password)
		repo_url = getRepoURL(gitobj, repo_name)

		if repo_url is not None:
			if not folderExists(repo_name):
				# we should pull the repo
				os.system("git clone %s" % repo_url)			
			else:
				#maybe try to reconcile local and remote folders?
				print "this already exists locally!"
		else:
			if not folderExists(repo_name):
				# make github repo, make folder, git init, set remote
				repo = createRepo(gitobj, repo_name)
				os.system("git clone %s" % repo.git_url)
			else:
				# make github repo, git init, push local content
				print "this already exists locally!"

if __name__ == '__main__':
	main(sys.argv)