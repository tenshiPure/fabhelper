from fabric.decorators import task

from fabhelper import cron

@task
def echo_to_directory():
	cron.echo_to_directory('vagrant', cron.daily, 'touch /tmp/echo_to_directory_`date +\%Y\%m\%d\%H\%M\%S`', 'echo_to_directory.sh')


@task
def put_to_directory():
	import os.path
	shell = '%s/../localfiles/put_to_directory.sh' % os.path.dirname(__file__)
	cron.put_to_directory('vagrant', cron.daily, shell)


@task
def echo_to_spool():
	cron.echo_to_spool('vagrant', '* * * * * touch /tmp/echo_to_spool_`date +\%Y\%m\%d\%H\%M\%S`')


@task
def all():
	echo_to_directory()
	put_to_directory()
	echo_to_spool()
