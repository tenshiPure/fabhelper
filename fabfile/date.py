from fabric.decorators import task

from fabhelper import date

@task
def now():
	print date.now()


@task
def now_with_format():
	print date.now('%Y%m%d')
