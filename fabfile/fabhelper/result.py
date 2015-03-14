from fabric.api import sudo, hide

from configure import result

def done(command, bold = False):
	color = result.done
	__print(color, bold, command)


def error(command, bold = False):
	color = result.error
	__print(color, bold, command)


def already(command, bold = False):
	color = result.already
	__print(color, bold, command)


def __print(color, bold, command):
	with hide('everything'):
		print color(sudo(command), bold)
