from fabric.decorators import task

from fabhelper import yum

@task
def install_package():
	yum.install('wget')

@task
def install_packages():
	yum.install(['wget', 'tree'])
