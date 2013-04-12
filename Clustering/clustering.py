#-*- coding:utf-8 -*-

import numpy
import scipy
import matplotlib.pyplot as pyplot
import random
import cPickle as cpickle

class Kmeans(object):
	"""docstring for Kmeans"""
	p = 0

	center_update = 0

	def __init__(self, k ,source,threshold = 0.002):
		super(Kmeans, self).__init__()
		self.dimension = len(source[0])
		self.k = k
		
		self.threshold = threshold
		self.centers = numpy.array( [ value for value in random.sample(source,k)] )
		self.source = numpy.zeros( (len(source),self.dimension + 1) )

		for i in range(0,len(source)):
			for j in range(0,self.dimension):
				self.source[i][j] = source[i][j]
			self.source[i][self.dimension] = int( random.uniform(0,k) )

	def exe(self):
		J = 1.
		ite = 0
		while J > self.threshold:
			ite += 1
			print 'iteration time->',ite
			self.update_cluster()
			self.update_centers()
			self.snapshot(movieclicks = ite)
			J = self.cost()

			if ite > 12:
				break
		return self.source[:,self.dimension].tolist()

	
	def cost(self):
		J = 0.
		for i in range(0,len(self.source)):

			J += numpy.linalg.norm(self.source[i][0:self.dimension] - self.centers[ int(self.source[i][self.dimension]) ] )
	
		return J

	def update_cluster(self):
		distance = [value for value in range(0,self.k)]

		for position,point in enumerate(self.source):

			for i in range(0,self.k):
				distance[i] = numpy.linalg.norm( point[0:self.dimension] - self.centers[i] )
			center = min(distance)

			self.source[position][self.dimension] = distance.index(center)

	def update_centers(self):
		center_counter = [0 for value in range(0,self.k)]
		center_point = numpy.zeros( (self.k,self.dimension) )

		for i in range(0,len(self.source)):

			center_point[int(self.source[i][self.dimension])] += self.source[i][0:self.dimension]

			center_counter[ int(self.source[i][self.dimension])] += 1

		self.centers = numpy.array( [center_point[i] / center_counter[i]  for i in range(0,len(center_point))])

	def snapshot(self,movieclicks = 6):
		#colors = [[random.random(),random.random(),random.random()] for value in range(0,self.k)]
		colors = [ [1,0,0],[0,1,0],[0,0,1]]
		pcolors = [ colors[ int(self.source[value][self.dimension]) ] for value in range(0,len(self.source))]

		pyplot.plot(hold = False)
		pyplot.hold = True

		pyplot.scatter(self.source[:,0],self.source[:,1], c = pcolors)
		pyplot.savefig('iter%s.png' %movieclicks,format = 'png')

		pass

'''
#create the sample points and save them into the plk file
sample = open('sample.plk','r')
if len(sample.read()) == 0:
	sample.close()
	sample = open('sample.plk','w')
	obj = [ ( random.uniform(0,10),random.uniform(0,10) ) for value in range(0,100)]
	f = cpickle.dump(obj,sample)
	print type(f)
else:
	pass
'''
if __name__ == '__main__':
	#create samples
	sample = open('sample.plk','r')
	points = cpickle.load(sample)

	kmeans = Kmeans(3,points)
	kmeans.exe()

	print 'ok'
	sample.close()

