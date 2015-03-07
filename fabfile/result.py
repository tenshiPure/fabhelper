from fabric.decorators import task

from fabhelper import result

@task
def ok():
	result.ok('uname -a')
	result.ok('echo some string')


@task
def ng():
	result.ng('uname -a')
	result.ng('echo some string')
