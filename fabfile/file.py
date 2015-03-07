from fabric.decorators import task

from fabhelper import file

@task
def sed():
	file.sed('/tmp/sample.txt', 'hoge', 'aaaaa')
	file.sed('/tmp/sample.txt', 'fuga', 'bbbbb')


@task
def sed_e():
	file.sed('/tmp/sample.txt', '^hoge', 'aaaaa', e = True)


@task
def conf():
	__sed_with_conf('/tmp/sample.txt')


@file.conf
def __sed_with_conf(path):
	file.sed(path, 'hoge', 'aaaaa')
	file.sed(path, 'fuga', 'bbbbb')
