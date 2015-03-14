from fabric.decorators import task
from fabric import colors

from fabhelper import result, configure

@task
def done():
	result.done("echo 'done    : default color'")


@task
def error():
	result.error("echo 'error   : default color'")


@task
def already():
	result.already("echo 'already : default color'")


@task
def change_color():
	configure.result.done = colors.blue
	result.done("echo 'done    : change configure'")
	configure.result.done = colors.green


@task
def bold():
	result.done("echo 'done    : bold'", bold = True)


@task
def all():
	done()
	error()
	already()

	change_color()

	bold()
