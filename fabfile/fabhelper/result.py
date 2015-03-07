from fabric.api import run, hide
from fabric.colors import green, red

def ok(command):
	__print(green, command)

def ng(command):
	__print(red, command)

def __print(color, command):
	with hide('everything'):
		print color(run(command))
