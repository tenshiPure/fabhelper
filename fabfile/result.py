from fabric.decorators import task

from fabhelper import result

@task
def done():
	result.done('uname -a')
	result.done('echo some string')


@task
def error():
	result.error('uname -a')
	result.error('echo some string')


@task
def already():
	result.already('uname -a')
	result.already('echo some string')


@task
def all():
	done()
	error()
	already()
