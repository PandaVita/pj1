import random
from collections import Counter
import math

import numpy as np

def generate(total, target):
	"""docstring for Generate"""
	values = np.zeros(total, dtype= int)
	targetList = random.sample(range(0, total), target)
	values[targetList] = 1
	#values = values.tolist()
	return values		

def catch(values, target, size):
	count = 0 #得测多少次
	num = 0 #num是找出了多少个
	times = len(values)//size #除去余数后values的总长度能被拿多少次
	remainder = len(values)%size #余数
	values = np.array(values)
	end = np.array([])
	if size == 1:
		return len(values)
	
	#如果values的数量能被size整除，进行reshape
	if remainder == 0:
		new_values = values.reshape(-1, size)
	else:
		new_values = values[:0-remainder].reshape(-1,size)
		end = values[-remainder:]
		count += 1
	#对values第二维度进行降维求和
	val_sum = new_values.sum(axis = 1).astype(int)
	end_sum = end.sum()
	if len(end) == 1:
		num += 1 if end != 0 else 0
	elif end_sum != 0:
		num += end_sum
		count += len(end)
	
	for x in np.nditer(val_sum):
		if num == target:
			break;
		elif x != 0:
			count += size
			num += x

	return count + times

def add_to_dic(result, dic):
	if dic.__contains__(result):
		dic[result] += 1
	else:
		dic[result] = 1

if __name__ == '__main__':
	
	a = catch([1,-1,1,-1,1,1,-1,1,1,1,-1],4,3)
	print(a)