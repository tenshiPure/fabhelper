from fabric.api import run, hide

from result import done

def clone(repository, dst, branch = 'master'):
	with hide('stdout'):
		run('git clone -b %s %s %s' % (branch, repository, dst))
	done("echo -n 'complete clone : '; ls -ld %s" % dst)
	done("echo -n 'branch         : '; cd %s; git rev-parse --abbrev-ref HEAD" % dst)
