from fabric.decorators import task

from fabhelper import git

@task
def clone():
	repository = 'https://github.com/tenshiPure/infrastructure.git'
	dst = '/tmp/infrastructure'
	git.clone(repository, dst)


@task
def clone_with_branch_specify():
	repository = 'https://github.com/tenshiPure/infrastructure.git'
	dst = '/tmp/infrastructure'
	branch = 'envassert'
	git.clone(repository, dst, branch)
