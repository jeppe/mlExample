#-*- coding:utf-8 -*-

def loader(direct):
		label = []
		points = []
		with open(direct,'r') as df:
			for line in df.readlines():
				line = line.strip().split(' ')
				label.append(float(line[0]))
				x_feature = float(line[1][2:])
				y_feature = float(line[2][2:])

				points.append([x_feature,y_feature])
			df.close()
		return label,points
