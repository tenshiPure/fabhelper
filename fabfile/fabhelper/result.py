from fabric.api import sudo, hide, env

from fabric import colors

green   = colors.green
red     = colors.red
cyan    = colors.cyan
blue    = colors.blue
magenta = colors.magenta
yellow  = colors.yellow
white   = colors.white

def done(command, bold = False, color = colors.green):
	color = env.get('_done_color', color)
	__print(color, bold, command)


def error(command, bold = False, color = colors.red):
	color = env.get('_error_color', color)
	__print(color, bold, command)


def already(command, bold = False, color = colors.cyan):
	color = env.get('_already_color', color)
	__print(color, bold, command)


def set_color_done(color):
	env._done_color = color


def set_color_error(color):
	env._done_error = color


def set_color_already(color):
	env._done_already = color


def reset_color_done():
	__reset('done')


def reset_color_error():
	__reset('error')


def reset_color_already():
	__reset('already')


def reset_color_all():
	reset_color_done()
	reset_color_error()
	reset_color_already()


def __reset(kind):
	try:
		env.pop('_%s_color' % kind)
	except:
		pass


def __print(color, bold, command):
	with hide('everything'):
		print color(sudo(command), bold)
