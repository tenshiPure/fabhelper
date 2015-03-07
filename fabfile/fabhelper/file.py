from fabric.api import sudo

from result import ok

def sed(path, src, dst, e = False):
	option = ['-i', '-ie'][e]

	sudo("sed %s 's/%s/%s/' %s" % (option, __escape(src), __escape(dst), path))


def __escape(string):
	return string.replace('/', '\/').replace('"', '\"')
