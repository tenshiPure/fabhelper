from fabric.api import sudo, hide

from result import done, already
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
		done("echo 'stopped         : %s'" % service)
	else:
		already("echo 'already stopped : %s'" % service)


def __isRunning(service):
	with hide('everything'):
		status = sudo('service %s status; true' % service)
		return 'running' in status or 'enabled' in status


def off(target):
	[__off(service) for service in toList(target)]


def __off(service):
	if __isOn(service):
		with hide('everything'):
			sudo('chkconfig %s off' % service)
		done("echo 'turn off        : %s'" % service)
	else:
		already("echo 'already off     : %s'" % service)


def __isOn(service):
	with hide('everything'):
		return '3:on' in sudo('chkconfig --list %s; true' % service)


def to_enabled(target):
	start(target)
	on(target)


def start(target):
	[__start(service) for service in toList(target)]


def __start(service):
	if __isRunning(service):
		already("echo 'already started : %s'" % service)
	else:
		with hide('everything'):
			sudo('service %s start' % service)
		done("echo 'started         : %s'" % service)


def on(target):
	[__on(service) for service in toList(target)]


def __on(service):
	if __isOn(service):
		already("echo 'already on      : %s'" % service)
	else:
		with hide('everything'):
			sudo('chkconfig %s off' % service)
		done("echo 'turn on         : %s'" % service)


def restart(target):
	[__restart(service) for service in toList(target)]


def __restart(service):
	if __isRunning(service):
		sudo('service %s restart' % service)
	else:
		sudo('service %s start' % service)


def reload(target):
	[__reload(service) for service in toList(target)]


def __reload(service):
	sudo('service %s reload' % service)
