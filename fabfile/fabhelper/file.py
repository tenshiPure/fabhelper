from fabric.api import run, sudo

from result import ok

def sed(path, src, dst, e = False):
	option = ['-i', '-ie'][e]

	sudo("sed %s 's/%s/%s/' %s" % (option, __escape(src), __escape(dst), path))


def __escape(string):
	return string.replace('/', '\/').replace('"', '\"')


def conf(func):
	def _conf(path):
		__backup(path)
		func(path)
		__diff(path)

	return _conf


def __backup(path):
	if 'No such file or directory' in sudo('ls %s.origin; true' % path):
		sudo('cp -p %s %s.origin' % (path, path))
		ok('echo create backup : %s.origin' % path)
	else:
		ok('echo %s.origin is already exists' % path)


def __diff(path):
	ok('diff %s %s.origin; true' % (path, path))


def link(src, dst):
	run('ln --symbolic --force %s %s' % (src, dst))
	ok('ls -l %s' % dst)
	ok('ls -l %s' % src)
