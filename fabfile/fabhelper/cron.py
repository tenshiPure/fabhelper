import os.path

from fabric.api import sudo, put, hide

from result import done

hourly  = '/etc/cron.hourly'
daily   = '/etc/cron.daily'
weekly  = '/etc/cron.weekly'
monthly = '/etc/cron.monthly'
spool   = '/var/spool/cron'


def echo_to_directory(user, directory, shell_line, shell_name):
	path = '%s/%s' % (directory, shell_name)
	sudo("echo '%s' > %s" % (shell_line, path))
	__chmod(path)
	__chown(user, path)
	done("echo -n 'create shell : '; ls -l %s" % path)


def put_to_directory(user, directory, shell):
	path = '%s/%s' % (directory, os.path.basename(shell))
	put(shell, directory,  use_sudo = True)
	__chmod(path)
	__chown(user, path)
	done("echo -n 'send shell   : '; ls -l %s" % path)


def echo_to_spool(user, line):
	path = '%s/%s' % (spool, user)
	sudo("echo '%s' >> %s" % (line, path))
	__chown(user, path)
	done("echo -n 'create shell : '; ls -l %s" % path)


def __chmod(path):
	sudo('chmod 755 %s' % path)


def __chown(user, path):
	sudo('chown %s:%s %s' % (user, user, path))
