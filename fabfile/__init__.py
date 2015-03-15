from fabric.decorators import task

from fabhelper.configure import set_ssh_env
set_ssh_env('sample_vagrant')

import result
import yum
import service
import file
import date
import git
import cron
import log

@task
def all():
	result.all()
	yum.all()
	service.all()
	file.all()
	date.all()
	git.all()
	cron.all()
	log.all()
