from github import Github, GithubException, BadCredentialsException

def getGithub(username, password):
	gitobj = Github(username, password)
	try:
		if "hello" in gitobj.get_user().get_repos():
			pass
	except BadCredentialsException, e:
		return None
	return gitobj

def repoExists(gitobj, repo):
	if repo in gitobj.get_user().get_repos():
		return True
	else:
		return False
