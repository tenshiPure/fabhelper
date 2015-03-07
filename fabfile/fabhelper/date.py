from fabric.api import run, hide

def now(format = '%F_%T'):
	with hide('everything'):
		return run('date +%s' % format)
