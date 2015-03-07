from fabric.api import sudo, hide

from result import ok

def to_disabled(target):
	if type(target) is str:
		__stop(target)
		__off(target)
	else:
		[__stop(service) for service in target]
		[__off(service) for service in target]


def stop(target):
	if type(target) is str:
		__stop(target)
	else:
		[__stop(service) for service in target]


def __stop(service):
	if __isRunning(service):
		with hide('everything'):
			sudo('service %s stop' % service)
		ok('echo stop %s' % service)
	else:
		ok('echo %s is already stopped' % service)


def __isRunning(service):
	with hide('everything'):
		return 'running' in sudo('service %s status; true' % service)


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
