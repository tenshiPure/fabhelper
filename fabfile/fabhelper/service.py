from fabric.api import sudo, hide

from result import ok
from util import toList

def to_disabled(target):
	stop(target)
	off(target)


def stop(target):
	[__stop(service) for service in toList(target)]


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
	[__off(service) for service in toList(target)]


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
