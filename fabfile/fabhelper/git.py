from fabric.api import run, hide

def clone(repository, dst, branch = 'master'):
	with hide('stdout'):
		run('git clone -b %s %s %s' % (branch, repository, dst))
