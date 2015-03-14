from fabric.utils import _AttributeDict

git = _AttributeDict({
	'branch'  : 'development',
	'message' : 'no message.',
	'by'      : 'John Doe'
})

from fabric import colors

result = _AttributeDict({
	'done'    : colors.green,
	'error'   : colors.red,
	'already' : colors.cyan
})
