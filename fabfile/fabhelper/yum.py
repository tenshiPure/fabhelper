from fabric.api import run, sudo, hide

from result import ok

def install(target):
	if type(target) is str:
		__install(target)
	else:
		[__install(package) for package in target]


def __install(package):
	if __isNotInstalled(package):
		with hide('stdout'):
			sudo('yum install -y %s' % package)
		ok('rpm -q %s' % package)
	else:
		ok('echo %s is already installed' % package)


def __isNotInstalled(package):
	with hide('everything'):
		return 'not installed' in run('rpm -q %s; true' % package)
