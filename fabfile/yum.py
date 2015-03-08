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
