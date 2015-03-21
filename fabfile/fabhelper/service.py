from fabric.api import hide

from util import execute

from result import done, error, already
from util import iterate

def to_disabled(target):
	stop(target)
	off(target)


def stop(target):
	[__stop(service) for service in iterate(target)]


def __stop(service):
	if __isRunning(service):
		with hide('everything'):
			execute('service %s stop' % service)
		done("echo 'stopped         : %s'" % service)
	else:
		already("echo 'already stopped : %s'" % service)


def __isRunning(service):
	with hide('everything'):
		status = execute('service %s status; true' % service)
		return 'running' in status or 'enabled' in status


def off(target):
	[__off(service) for service in iterate(target)]


def __off(service):
	if __isOn(service):
		with hide('everything'):
			execute('chkconfig %s off' % service)
		done("echo 'turn off        : %s'" % service)
	else:
		already("echo 'already off     : %s'" % service)


def __isOn(service):
	with hide('everything'):
		return '3:on' in execute('chkconfig --list %s; true' % service)


def to_enabled(target):
	start(target)
	on(target)


def start(target):
	[__start(service) for service in iterate(target)]


def __start(service):
	if __isRunning(service):
		already("echo 'already started : %s'" % service)
	else:
		with hide('everything'):
			stdout = execute('service %s start; true' % service)
			if 'unrecognized' in stdout:
				error("echo 'start error     : %s is unrecognized'" % service)
			else:
				done("echo 'started         : %s'" % service)


def on(target):
	[__on(service) for service in iterate(target)]


def __on(service):
	if __isOn(service):
		already("echo 'already on      : %s'" % service)
	else:
		with hide('everything'):
			stdout = execute('chkconfig %s on; true' % service)
			if 'No such file or directory' in stdout:
				error("echo 'turn on error   : %s is unrecognized'" % service)
			else:
				done("echo 'turn on         : %s'" % service)


def restart(target):
	[__restart(service) for service in iterate(target)]


def __restart(service):
	if __isRunning(service):
		stdout = execute('service %s restart' % service)
	else:
		__start(service)


def reload(target):
	[__reload(service) for service in iterate(target)]


def __reload(service):
	stdout = execute('service %s reload; true' % service)
	if 'unrecognized' in stdout:
		error("echo 'reload error : %s is unrecognized'" % service)
