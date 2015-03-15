from fabric.utils import _AttributeDict

from fabric.api import run

execute = _AttributeDict({
	'func' : run
})

ssh = _AttributeDict({
	'server_name' : {
		'hosts'    : '',
		'user'     : '',
		'password' : '',
	}
})

from fabric import colors

result = _AttributeDict({
	'done'    : colors.green,
	'error'   : colors.red,
	'already' : colors.cyan
})

git = _AttributeDict({
	'branch'  : 'development',
	'message' : 'no message.',
	'by'      : 'John Doe'
})
