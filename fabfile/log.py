from fabric.decorators import task

from fabhelper import log

@task
def write_success():
	log.write_success('/tmp', 'sample.log', '%F', 'sample log line')


@task
def write_error():
	log.write_error('/tmp', 'sample.log', '%F', 'sample log line')


@task
def read_success():
	log.read_success('/tmp', 'sample.log', '2015-03-08')


@task
def read_error():
	log.read_error('/tmp', 'sample.log', '2015-03-08')


@task
def all():
	write_success()
	read_success()
	write_error()
	read_error()
