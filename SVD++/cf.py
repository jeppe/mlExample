#*- coding:utf-8 -*-
import random
import vector
import recommendation
from  math import sqrt

'''
	seperate @param:records into two dataset,they're trainset and testset.
	choose randomly 90%	of records to trainset,the lfet 10% 	to testset

	@param:customer is a dict,key is the id of each user.value is a embed
	dict,because we present what items the user has and the latent factor
	vector,'items' for the item he/she bought,'feature' presents the key 
	of features,its value is a list with constant length.

	@param:tester is a dict,key is the id of each user,value is a list
	including the deleted links

	@param:item_warehouse,a dict whose key is id of each item,value is a embed
	dict including 'score' and 'feature
'''

dimention = 10

customer =dict()
tester   = dict()
train_dict = dict()

'''building user objects and item warehous 
'''
with open('./ua_train.txt','r') as train:
	for link in train.readlines():
		link = link.strip()
		link = link.split('	')
		if link[0] not in customer:
			customer[link[0]] = {'feature':[random.uniform(0.0,value / value) for value in range(1,dimention + 1)]
								,'items':{link[1]:float(link[2]) }}
		else:
			if link[1] not in customer[link[0]]['items']:
				customer[link[0]]['items'][link[1]] = float(link[2])

with open('./ua_test.txt','r') as test:

	for link in test.readlines():
		link = link.strip()
		link = link.split('	')

		if link[0] not in tester:
			tester[link[0]] = {link[1]:float(link[2])}
		else:
			tester[link[0]][link[1]] = float(link[2])


print len(customer),len(tester)


#building the item_warehouse and execute SGD to update features of user and item

item_warehouse = dict()
speed = 0.01
penalty = 0.001

datas = open('./ua_train.txt','r')

for link in datas.readlines():
	link  = link.strip()

	link  = link.split('	')
#	if int(link[2]) >= 3:
	if link[1] not in item_warehouse:
		item_warehouse[link[1]] = {'score':0.0,'feature':[random.uniform(0,value / value) for value in range(1,dimention + 1)]}

	recommendation.SGD(customer,item_warehouse,link,speed,penalty)


ranking_score = 0.0
rmse    = 0.0
test_records = 0
counter = 0
for user in customer:
	counter += 1
	recommendation.init_item_warehouse(item_warehouse)
	for item in item_warehouse:
		if item not in customer[user]['items']:
			item_warehouse[item]['score'] = vector.dot(customer[user]['feature'],item_warehouse[item]['feature'])

	if user in tester:
		result = recommendation.rmse(tester[user],item_warehouse)
		rmse += result[0]
		test_records += result[1]

print rmse,test_records
print rmse * 1.0 / test_records

'''	if user in tester:
		test_records += len(tester[user])
		for titem in tester[user]:
			rs = recommendation.rankingscore(customer[user],titem,item_warehouse)

			ranking_score += rs


print ranking_score / test_records

'''	