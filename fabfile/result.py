from fabric.decorators import task

from fabhelper import result

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
def done_change_color_specify_with_argument():
	result.done("echo 'done    : specify with argument'", color = result.blue)


@task
def done_change_color_specify_setter():
	result.set_color_done(result.magenta)
	result.done("echo 'done    : specify with setter'")
	result.reset_color_all()

	result.done("echo 'done    : default color'")

@task
def bold():
	result.done("echo 'done    : bold'", color = result.yellow, bold = True)


@task
def all():
	done()
	error()
	already()

	done_change_color_specify_with_argument()

	done_change_color_specify_setter()

	bold()
