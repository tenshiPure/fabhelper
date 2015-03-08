from fabric.api import run, hide

from result import done, error
from date import now
from file import isExists

def write_success(directory, file, format, line):
	path = '%s/%s.success.%s' % (directory, file, now(format))
	run('echo %s >> %s' % (line, path))
	done("echo 'write success log : %s >> %s'" % (line, path))


def write_error(directory, file, format, line):
	path = '%s/%s.error.%s' % (directory, file, now(format))
	run('echo %s >> %s' % (line, path))
	error("echo 'write error log   : %s >> %s'" % (line, path))


def read_success(directory, file, date):
	path = '%s/%s.success.%s' % (directory, file, date)
	if isExists(path):
		done("echo 'log lines         : %s'; echo '%s'" % (path, __read(path)))
	else:
		error("echo 'no such file : %s'" % path)


def read_error(directory, file, date):
	path = '%s/%s.error.%s' % (directory, file, date)
	if isExists(path):
		error("echo 'log lines         : %s'; echo '%s'" % (path, __read(path)))
	else:
		error("echo 'no such file : %s'" % path)


def __read(path):
	with hide('everything'):
		return run('cat %s' % path)
