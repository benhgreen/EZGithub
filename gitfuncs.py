from github import Github, GithubException, BadCredentialsException

def getGithub(username, password):
	username = username.replace('\n', '')
	password = password.replace('\n', '')
	gitobj = Github(username, password)
	try:
		if "hello" in gitobj.get_user().get_repos():
			pass
	except BadCredentialsException, e:
		return None
	return gitobj

def getRepoURL(gitobj, name):
	for repo in gitobj.get_user().get_repos():
		if name == repo.name:
			return repo.git_url
	return None

def printRepos(gitobj):
	for repo in gitobj.get_user().get_repos():
		print repo.name

# create github repo on github!
def createRepo(gitobj, name):
	description = raw_input("Enter a short description of this repo: ")
	return gitobj.get_user().create_repo(name, description=description, auto_init=True)
