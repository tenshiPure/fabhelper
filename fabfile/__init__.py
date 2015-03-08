from fabric.api import env

env.hosts = ['192.168.100.10']
env.user = 'vagrant'
env.password = 'vagrant'

import result
import yum
import service
import file
import date
import git
import cron

from fabric.decorators import task

@task
def all():
	result.all()
	yum.all()
	service.all()
	file.all()
	date.all()
	git.all()
	cron.all()
