import vector
import random #used for evaluating


'''this model gathers many recommendation algorithm and models'''


'''
	initilization	
'''
def init_item_warehouse(items):
	for value in items:
		items[value]['score'] = 0.0

'''
	Function SGD:Navie Stochatic Gradient Descent ,which is alwarys used to 
	get the optimized answer to square loss function.

	@record in SGD means SGD function will updated the user and item's 
	feature vector included in it.It includes two elements,firt element 
	is the user ID,second is the item ID and the value passed to
	 SGD must base on the rule  

	@items:a dict include all the items found by the users

	@users:a dict contains all users

	@speed:it defines the speed from current point runs to next point

	@penalty:it descides the weight of the term in the loss function of Matrix
	Factorization
'''

def SGD(users,items,record,speed,penalty):
	'''
		Pu is the user's feature vector
		Qi is the item's feature vector
		e  is the prediction error
		the default rate for each is 1
		SGD will iterate update Pu and Qi based on the following:
			Pu <--- Pu + speed * (e * Qi - penalty * Pu)
			Qi <--- Qi + speed * (e * Pu - penalty * Qi)
	'''

	Pu = users[record[0]]['feature']
	Qi = items[record[1]]['feature']
	

	e = float(record[2]) - vector.dot(Pu,Qi)

	pu = vector.plus(Pu , vector.num_dot(speed , vector.sub(vector.num_dot(e , Qi) , vector.num_dot(penalty , Pu) ) ) )
	Qi = vector.plus(Qi , vector.num_dot(speed , vector.sub(vector.num_dot(e , Pu) , vector.num_dot(penalty , Qi) ) ) )
	Pu = pu

	users[record[0]]['feature'] = Pu
	items[record[1]]['feature'] = Qi


'''
	we need the recommendation algorithm and model,also need some rules to 
	evaluate whether our predictor is good or not.
'''

def rankingscore(user,item,item_warehouse):
	_choose = 2000
	rank_score = 0.0
	item_score = item_warehouse[item]['score']

	#print item_score
	items = item_warehouse.items()
	customer_item = user['items']

	while _choose > 0:
		ran_item = random.choice(items)
		if ran_item[0] not in customer_item:
			if ran_item[0] != item:
				_choose -= 1
				if ran_item[1]['score'] > item_score:
					rank_score += 1.0
				elif ran_item[1]['score'] == item_score:
					rank_score += 0.5

	return rank_score / 2000.0

def rmse(items_test,item_warehouse):
	
	rmse = 0.
	record = 0
	for item in items_test:
		if item in item_warehouse:
			record += 1
			rmse += abs(item_warehouse[item]['score'] - items_test[item] )


	return [rmse,record]
