#-*- coding:utf-8 -*-
import numpy,random
from math import sqrt

class Autoencoder(object):
	"""docstring for Autoencoder"""
	def __init__(self, visible = 7, hidden = 5,bvis = None,bhid = None):
		super(Autoencoder, self).__init__()
		self.n_visible = visible
		self.n_hidden = hidden

		#initialize the weight matrix
		self.W_in = numpy.random.uniform(low = (- 6. / sqrt(visible + hidden + 1)),
								high = (6. / sqrt(visible + hidden + 1)),size = (hidden,visible))
		
		self.W_out = self.W_in.copy().T
		
		if not bvis:
			self.bvis = numpy.zeros((1,hidden))
		if not bhid:
			self.bhid = numpy.zeros((1,visible))

		self.params = [self.W_in,self.bvis,self.W_out,self.bhid]

	def loadata(self,datas):
		pass

	def cost(self):
		pass

	def gradient_check(self):
		pass

	def normalization(self,datas):
		pass
		