from fabric.decorators import task

from fabhelper import yum

@task
def install_package():
	yum.install('wget')


@task
def install_packages():
	yum.install(['wget', 'tree'])


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
