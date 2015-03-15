def iterate(target):
	if type(target) == str:
		return [target]
	elif type(target) == tuple:
		return [target]
	elif type(target) == list:
		return target
	else:
		raise Exception('invalid argument. string, tuple, list are allowed.')


def execute(command):
	from configure import execute
	return execute.func(command)


# temporary test
if __name__ == '__main__':
	s1 = 'wget'
	s2 = 'tree'
	print iterate(s1)
	print iterate([s1, s2])

	t1 = ('key', 'val')
	t2 = ('req', 'res')
	print iterate(t1)
	print iterate([t1, t2])

	invalid1 = 1
	invalid2 = None
	invalid3 = lambda x: x
	try:
		iterate(invalid1)
	except:
		print 'invalid'
	try:
		iterate(invalid2)
	except:
		print 'invalid'
	try:
		iterate(invalid3)
	except:
		print 'invalid'
