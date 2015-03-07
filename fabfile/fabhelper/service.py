from fabric.api import run, sudo, hide

from result import ok

def off(target):
	if type(target) is str:
		__off(target)
	else:
		[__off(service) for service in target]


def __off(service):
	if __isOn(service):
		with hide('everything'):
			sudo('chkconfig %s off' % service)
		ok('echo turn off %s' % service)
	else:
		ok('echo %s is already off' % service)


def __isOn(service):
	with hide('everything'):
		return '3:on' in sudo('chkconfig --list %s; true' % service)
