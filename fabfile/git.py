from fabric.decorators import task

from fabhelper import git

@task
def clone():
	repository = 'https://github.com/tenshiPure/fabhelper.git'
	dst = '/tmp/fabhelper'
	git.clone(repository, dst)


@task
def clone_with_branch_specify():
	repository = 'https://github.com/tenshiPure/infrastructure.git'
	dst = '/tmp/infrastructure'
	branch = 'envassert'
	git.clone(repository, dst, branch)


@task
def all():
	clone()
	clone_with_branch_specify()
