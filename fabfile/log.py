from fabric.api import run
from fabric.decorators import task

from fabhelper import log

@task
def prepare():
	run("rm /tmp/*.log")


@task
def write_success():
	log.write_success('/tmp/success.log', 'sample success log line')


@task
def write_error():
	log.write_error('/tmp/error.log', 'sample error log line')


@task
def read_success():
	log.read_success('/tmp/success.log')


@task
def read_error():
	log.read_error('/tmp/error.log')


@task
def all():
	prepare()
	write_success()
	read_success()
	write_error()
	read_error()
