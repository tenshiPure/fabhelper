from fabric.api import run
from fabric.decorators import task

from fabhelper import file

@task
def prepare():
	run("echo -e 'hoge\nfuga\n#hoge' > /tmp/sample.txt")
	run("rm -rf /tmp/samples; mkdir -p /tmp/samples; cd /tmp/samples; touch {1,2,3,4,5}{a,b,c,d,e}")


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
	__sed_with_conf('/invalid/path')


@file.conf
def __sed_with_conf(path):
	file.sed(path, 'hoge', 'aaaaa')
	file.sed(path, 'fuga', 'bbbbb')


@task
def link():
	file.link('/tmp/sample.txt', '/tmp/sample.txtlink')
	file.link('/tmp/samples', '/tmp/sampleslink')
	file.link('/invalid/path', '/tmp/sample.txtlink')


@task
def clean():
	file.cleanUp('/tmp/samples', 5)


@task
def all():
	prepare()
	conf()
	link()
