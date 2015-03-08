from fabric.api import sudo, hide
from fabric.colors import green, red, cyan

def done(command):
	__print(green, command)


def error(command):
	__print(red, command)


def already(command):
	__print(cyan, command)


def __print(color, command):
	with hide('everything'):
		print color(sudo(command))
