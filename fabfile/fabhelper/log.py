from fabric.api import hide

from util import execute

from result import done, error
from file import isExists, cat

def write_success(path, line):
	__write(path, line, done)


def write_error(path, line):
	__write(path, line, error)


def __write(path, line, func):
	execute('echo %s >> %s' % (line, path))
	func("echo 'write log   : %s >> %s'" % (line, path))


def read_success(path):
	__read(path, done)


def read_error(path):
	__read(path, error)


def __read(path, func):
	try:
		lines = cat(path)
		func("echo 'log lines         : %s'; echo '%s'" % (path, lines))

	except AssertionError as e:
		error("echo 'no such file : %s'" % path)
