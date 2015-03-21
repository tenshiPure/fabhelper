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
	service.stop('postfix')


@task
def stop_services():
	service.stop(['postfix', 'crond'])


@task
def off_service():
	service.off('postfix')


@task
def off_services():
	service.off(['postfix', 'crond'])


@task
def to_enabled_service():
	service.to_enabled('postfix')


@task
def to_enabled_services():
	service.to_enabled(['postfix', 'crond', 'invalid'])


@task
def start_service():
	service.start('postfix')


@task
def start_services():
	service.start(['postfix', 'crond'])


@task
def on_service():
	service.on('postfix')


@task
def on_services():
	service.on(['postfix', 'crond'])


@task
def restart_service():
	service.restart('crond')


@task
def restart_services():
	service.restart(['crond', 'crond'])


@task
def reload_service():
	service.reload('sshd')


@task
def reload_services():
	service.reload(['sshd', 'sshd'])


@task
def all():
	to_disabled_service()
	to_disabled_services()
	to_enabled_service()
	to_enabled_services()
	restart_service()
	restart_services()
	reload_service()
	reload_services()
