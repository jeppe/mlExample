import math

'''
	#functions:
		model:x vector calls vectorModel(x) wil return |x| of vector
		normalization: after vector x calls vectorNormalization(x),
							vector x's model will be 1
		dot:it will return x*y,x and y are both vector

		num_dot:it generate a vector result on multiplying each factor of a vector x by constant 
			@param:
				coefficient: means the constant
				x : a vector
		sub:return the result of x - y both x and y are vectors

		plus: return the result of x + y both x and y are vectors

'''

def model(x):
	mod = 0.0
	try:
		for value in range(0,len(x)):
			mod += float(x[value])**2
		return model
	except Exception, e:
		raise "error trying to visite a vector"
		return -1
def normalization(x):
	x_model = model(x)
	x = [value / x_model for value in x]

def dot(x,y):
	_dot = 0.
	if len(x) == len(y):
		try:
			for value in range(0,len(x)):
				_dot += x[value] * y[value]
#			if math.isnan(_dot):
#				print 'x ',x,'\n'
#				print 'y ',y,'\n'
#				raw_input()	
			return _dot	
		except:
			raise "vector dot error"
	else:
		raise "two vectors need the same dimensionality"

def num_dot(coefficient,x):
	num = [0.0]*len(x)
	for value in range(0,len(x)):
		num[value] = coefficient * x[value]

	return num

def plus(x,y):
	
	if len(x) == len(y):
		_plus = [0.0]*len(x)
		try:
			for value in range(0,len(x)):
				_plus[value] = x[value] + y[value]
			return _plus
		except:
			raise "vector plus error"
	else:
		raise "two vectors need the same dimensionality"

def sub(x,y):

	if len(x) == len(y):
		_sub = [0.0]*len(x)
		try:
			for value in range(0,len(x)):
				_sub[value] = x[value] - y[value]
			return _sub
		except:
			raise "vector sub error"
	else:
		raise "two vectors need the same dimensionality"