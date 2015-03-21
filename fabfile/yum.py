from fabric.decorators import task

from fabhelper import yum

@task
def update():
	yum.update()


@task
def cron():
	yum.cron()


@task
def install_package():
	yum.install('wget')


@task
def install_packages():
	yum.install(['wget', 'tree', 'invalid'])


@task
def all_install():
	install_package()
	install_packages()


@task
def addEpel():
	yum.addEpel()


@task
def addRemi():
	yum.addRemi()


@task
def addRpmForge():
	yum.addRpmForge()


@task
def all_repositories():
	addEpel()
	addRemi()
	addRpmForge()


@task
def install_package_with_repository():
	yum.addRemi()
	yum.install('php', 'remi')


@task
def install_package_with_repositories():
	yum.addRemi()
	yum.install('php', ['remi', 'remi-php55'])


@task
def install_packages_with_repository():
	yum.addRemi()
	yum.install(['php', 'mysql-server'], 'remi')


@task
def install_packages_with_repositories():
	yum.addRemi()
	yum.install(['php', 'mysql-server'], ['remi', 'remi-php55'])


@task
def all_install_with_repositories():
	install_package_with_repository()
	install_package_with_repositories()
	install_packages_with_repository()
	install_packages_with_repositories()


@task
def all():
	update()
	cron()
	all_install()
	all_repositories()
	all_install_with_repositories()
