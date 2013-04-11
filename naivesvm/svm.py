#-*- coding:utf-8 -*-

import matplotlib.pyplot as pyplot
from numpy import array,zeros
import dataloader
import random

class SVM(object):
	'''define svm class'''
	alpha = 1#define the contraint coefficient
	w     = 1#parameters of classifier
	label = 1#labels of oberservation
	points = 1#training points

	soft_defination = 3

	def __init__(self,label,points,soft_defination):
		self.dimension = dimension
		self.label     = label
		self.points    = points
		self.soft_defination = soft_defination

		self.alpha = [random.uniform(0,self.soft_defination) for i in xrange(0,len(label))]
		self.w     = [random.random() for i in xrange(0,len(points[0]))]

	def SMO(self):
		support_index = list()
		KKT_condition = True
		
		while KKT_condition != False:
			for index in xrange(0,len(self.alpha)):
				if 0 =< self.alpha(index) <= self.soft_defination:
					continue
				else:
					KKT_condition = False

		return support_index

	def observer(self,step = 1):
		color = array([[0,0,1], [1,0,0],[0,1,0] ] )

		#color for classifier
		datacolor = [color[lbl] for lbl in self.label]

		X= zeros(( len(self.label),len(self.points[0]) ))

		#init a the data matrix
		for i in xrange(0,len(self.label)):
			X[i][0],X[i][1] = self.points[i][0],self.points[i][1]
		#clear the previous figure
		pyplot.plot(hold = False)
		pyplot.hold = True

		pyplot.scatter(X[:,0],X[:,1],c = datacolor)
		pyplot.savefig("data/twofeature.png",format = "png")

	def get_label(self):
		return label
	def get_points(self):
		return points

if __name__ == "__main__":
	label,points = dataloader.loader("twofeature.txt")
	svm = SVM(label = label,points = points)
	svm.observer()
	