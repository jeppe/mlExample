#-*- coding:utf-8 -*-

import numpy
import scipy
import matplotlib.pyplot as pyplot
import random
import cPickle as cpickle

class Kmeans(object):
	""" docstring for Kmeans
		call it by 'kmeans = Kmeans(3,points)' and impelement it by calling kmeans.exe()
		Kmeans could return a label list,whose index is the id for each entity
	"""
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

			if ite > 15:
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

class SpectralCluster(object):
	"""docstring for SpectralCluster(SC)
		SC classify the items based on the item-item similarity matrix,which is denoted as A.
		First,we calculate the similarity between each pair of items.
		Second,construct a Laplace Matrix D. ( D = B - A ) B is a diagnose matrix,whose diagnose element
		is the sum of corresponding column of A
		Third,we acquire the eigenvalue of D and sort it by descenting order.
		Then,we also obtain the corresponding eigenvalue vectors of each eigenvalue,which is column vector.
		We organize them by the descenting order of the eigenvalue to build a matrix,each row of which is
		the feature for corresponding user.
		Finally,we only abstract the top-K columns and cluster them by k-means method. 
	"""

	def __init__(self, simatrix,K):
		super(SpectralCluster, self).__init__()
		self.simatrix = simatrix
		self.k = K
		self.dimension = len(simatrix[0])

	def matrixL(self):
		D = numpy.zeros( (self.dimension,self.dimension) )#define the diagnose matrix D
		for i in range(0,self.dimension):
			D[i][i] = self.simatrix[:,i].sum()
		L = D - self.simatrix#construct the Laplace Matrix
		evals,evec = numpy.linalg.eig(L)#return the eigenvalues and eigenvalues vectors
		idx = evals.argsort()
		evec = evec[:,idx]
		evec = evec[:,0:self.k]
		return evec

	def exe(self):
		kmeans= Kmeans( 3,self.matrixL() )
		labels = kmeans.exe()#impelement clustering
		return labels

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

	#kmeans = Kmeans(3,points)
	#kmeans.exe()

	sim = numpy.zeros( (len(points),len(points) ))	
	for i in range(0,len(points) - 1):
		for j in range(i+1,len(points)):
			sim[i][j] = points[i][0] - points[j][0]
			sim[j][i] = points[i][0] - points[j][0]

	SC = SpectralCluster(sim,3)
	labels = SC.exe()
	print labels
	sample.close()

