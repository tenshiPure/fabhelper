from fabric.decorators import task

from fabhelper import service

@task
def stop_service():
	service.stop('httpd')

@task
def stop_services():
	service.stop(['postfix', 'httpd'])

@task
def off_service():
	service.off('postfix')

@task
def off_services():
	service.off(['postfix', 'crond'])
