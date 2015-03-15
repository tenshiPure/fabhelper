from fabric.api import hide

from util import execute

def now(format = '%F_%T'):
	with hide('everything'):
		return execute('date +%s' % format)
