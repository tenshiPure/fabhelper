from fabric.api import run, sudo, hide

from result import done, already, error

def sed(path, src, dst, e = False):
	option = ['-i', '-ie'][e]

	sudo("sed %s 's/%s/%s/' %s" % (option, __escape(src), __escape(dst), path))


def __escape(string):
	return string.replace('/', '\/').replace('"', '\"')


def conf(func):
	def _conf(path):
		if __backup(path):
			func(path)
			__diff(path)

	return _conf


def __backup(path):
	if __hasNoBackup(path):
		if not isExists(path):
			error('echo not exists : %s' % path)
			return False
		else:
			with hide('everything'):
				sudo('cp -p %s %s.origin' % (path, path))
			done('echo create backup : %s.origin' % path)
			return True
	else:
		already('echo already exists : %s' % path)
		return True


def __hasNoBackup(path):
	with hide('everything'):
		return 'No such file or directory' in sudo('ls %s.origin; true' % path)


def __diff(path):
	done("echo 'diff'; diff %s %s.origin; true" % (path, path))


def link(src, dst):
	if not isExists(src):
		error('echo not exists : %s' % src)
	else:
		run('ln --symbolic --force %s %s' % (src, dst))
		done("echo -n 'link   : '; ls -l %s" % dst)
		done("echo -n 'origin : '; ls -l %s" % src)


def isExists(path):
	with hide('everything'):
		return path == sudo('ls -d %s; true' % path)


def isExistsLine(path, line):
	with hide('everything'):
		return line in sudo('cat %s; true' % path)
