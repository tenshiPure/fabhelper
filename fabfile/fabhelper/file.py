from fabric.api import run, sudo, hide

from result import done, already

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
	if __isNoBackup(path):
		with hide('everything'):
			sudo('cp -p %s %s.origin' % (path, path))
		done("echo 'create backup  : %s.origin'" % path)
	else:
		already("echo 'already exists : %s'" % path)


def __isNoBackup(path):
	with hide('everything'):
		return 'No such file or directory' in sudo('ls %s.origin; true' % path)


def __diff(path):
	done("echo 'diff'; diff %s %s.origin; true" % (path, path))


def link(src, dst):
	run('ln --symbolic --force %s %s' % (src, dst))
	done("echo -n 'link   : '; ls -l %s" % dst)
	done("echo -n 'origin : '; ls -l %s" % src)
