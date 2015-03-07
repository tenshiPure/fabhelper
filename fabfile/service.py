from fabric.decorators import task

from fabhelper import service

@task
def off_service():
	service.off('postfix')

@task
def off_services():
	service.off(['postfix', 'crond'])
