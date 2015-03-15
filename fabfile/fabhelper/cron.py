import os.path

from util import execute
from fabric.api import put, hide

from result import done, error
from file import isExists, isExistsLine

hourly  = '/etc/cron.hourly'
daily   = '/etc/cron.daily'
weekly  = '/etc/cron.weekly'
monthly = '/etc/cron.monthly'
spool   = '/var/spool/cron'


def echo_to_directory(user, directory, shell_line, shell_name):
	path = '%s/%s' % (directory, shell_name)

	if isExists(path):
		error('echo already exists : %s' % path)
	else:
		execute("echo '%s' > %s" % (shell_line, path))
		__chmod(path)
		__chown(user, path)
		done("echo -n 'create shell : '; ls -l %s" % path)


def put_to_directory(user, directory, shell, sudo = False):
	path = '%s/%s' % (directory, os.path.basename(shell))

	if isExists(path):
		error('echo already exists : %s' % path)
	else:
		put(shell, directory,  use_sudo = sudo)
		__chmod(path)
		__chown(user, path)
		done("echo -n 'send shell   : '; ls -l %s" % path)


def echo_to_spool(user, line):
	path = '%s/%s' % (spool, user)
	if isExistsLine(path, line):
		error('echo already exists : %s in %s' % (line, path))
	else:
		execute("echo '%s' >> %s" % (line, path))
		__chown(user, path)
		done("echo -n 'create shell : '; ls -l %s" % path)


def __chmod(path):
	execute('chmod 755 %s' % path)


def __chown(user, path):
	execute('chown %s:%s %s' % (user, user, path))
