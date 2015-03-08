from fabric.decorators import task

from fabhelper import service

@task
def to_disabled_service():
	service.to_disabled('httpd')


@task
def to_disabled_services():
	service.to_disabled(['postfix', 'httpd'])


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


@task
def restart_service():
	service.restart('crond')


@task
def restart_services():
	service.restart(['crond', 'crond'])


@task
def all():
	to_disabled_service()
	to_disabled_services()
	restart_service()
	restart_services()
