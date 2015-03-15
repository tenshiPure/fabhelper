import os
import os.path

from fabric.api import local, hide
from fabric.utils import _AttributeDict
from fabric.decorators import task


default = '%s/my_configure.py' % os.getcwd()
which = None

if os.path.exists(default):
	import my_configure as current_conf
	which = 'your configure.py'
else:
	import default_configure as current_conf
	which = 'default configure.py'

ssh = current_conf.ssh
result = current_conf.result
git = current_conf.git

@task
def generate():
	from result import done, already

	dst = '%s/my_configure.py' % os.getcwd()
	src = os.path.join(os.path.dirname(__file__), 'default_configure.py')

	if os.path.exists(dst):
		already('echo already exists  : %s' % dst)
	else:
		with hide('everything'):
			local('cp %s %s' % (src, dst))
		done('echo cteate complete : %s' % dst)


@task
def check():
	print '\n%s is loaded.' % which

	print '\nssh configure'
	print ssh

	print '\nresult configure'
	print result

	print '\ngit configure'
	print git


def set_ssh_env(key):
	from fabric.api import env
	env.update(ssh[key])
