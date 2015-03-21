from fabric.api import hide

from util import execute

from result import done, error
from file import isExists

def clone(repository, dst, branch = 'master'):
	if isExists(dst):
		error('echo already exists : %s' % dst)
	else:
		with hide('stdout'):
			stdout = execute('git clone -b %s %s %s; true' % (branch, repository, dst))
			if '403 Forbidden' in stdout:
				error("echo -n 'clone error    : 403 Forbidden'")
			else:
				if 'warning: Remote branch %s not found' % branch in stdout:
					error("echo -n 'warning        : %s dones not found'" % branch)
				done("echo -n 'complete clone : '; ls -ld %s" % dst)
				done("echo -n 'branch         : '; cd %s; git rev-parse --abbrev-ref HEAD" % dst)
