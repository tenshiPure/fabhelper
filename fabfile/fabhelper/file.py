from fabric.api import hide

from util import execute

from result import done, error, already

def sed(path, src, dst, e = False):
	if not isExists(path):
		error('echo not exists : %s' % path)
		return

	option = ['-i', '-ie'][e]

	execute("sed %s 's/%s/%s/' %s" % (option, __escape(src), __escape(dst), path))


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
				execute('cp -p %s %s.origin' % (path, path))
			done('echo create backup : %s.origin' % path)
			return True
	else:
		already('echo already exists : %s' % path)
		return True


def __hasNoBackup(path):
	with hide('everything'):
		return 'No such file or directory' in execute('ls %s.origin; true' % path)


def __diff(path):
	done("echo 'diff'; diff %s %s.origin; true" % (path, path))


def link(origin, link):
	if not isExists(origin):
		error('echo not exists : %s' % origin)
	else:
		execute('ln --symbolic --force %s %s' % (origin, link))
		done("echo -n 'link   : '; ls -l %s" % link)


def isExists(path):
	with hide('everything'):
		return path == execute('ls -d %s; true' % path)


def isExistsLine(path, line):
	with hide('everything'):
		return line in execute('cat %s; true' % path)

def cat(path):
	assert isExists(path)

	with hide('everything'):
		return execute('cat %s' % path)


def cleanUp(path, upperLimit):
	targets = __directoriesSortedByOlder(path)[:-upperLimit]
	[execute('rm -rf %s/%s' % (path, target)) for target in targets]


def __directoriesSortedByOlder(path):
	with hide('everything'):
		return execute('ls %s | sort' % path).split('\r\n')
