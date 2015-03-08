from fabric.api import run, hide

from result import done, error
from file import isExists

def clone(repository, dst, branch = 'master'):
	if isExists(dst):
		error('echo already exists : %s' % dst)
	else:
		with hide('stdout'):
			run('git clone -b %s %s %s' % (branch, repository, dst))
		done("echo -n 'complete clone : '; ls -ld %s" % dst)
		done("echo -n 'branch         : '; cd %s; git rev-parse --abbrev-ref HEAD" % dst)
