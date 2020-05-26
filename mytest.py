import time
import threading
import pygal


from mytool2 import generate, catch, add_to_dic


total = 1000000
targetRate = 0.002
target = int(total*targetRate)
size = 20
testTimes = 10000

results_dic = {}
time1 = time.time()

#-----这段为主程序使用多线程---------
#count = 0
# def testone(testTimes,total,target,size,dic,count):
# 	while count <testTimes:
# 		values = generate(total= total, target= target)
# 		result = catch(values= values, target = target, size = size)
# 		add_to_dic(result= result, dic = results_dic)
# 		count += 1

# class myThread(threading.Thread):
# 	def __init__(self, threadID, name, testTimes,total,target,size,dic,count):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.testTimes = testTimes
# 		self.total = total
# 		self.target = target
# 		self.size = size
# 		self.dic = dic
# 		self.count = count
# 	def run(self):
# 		threadLock.acquire()
# 		testone(self.testTimes,self.total,self.target,self.size,self.dic,self.count)
# 		threadLock.release()

# threadLock = threading.Lock()
# threads = []
# thread1 = myThread(1,'thread1',testTimes,total,target,size,results_dic,count)
# thread2 = myThread(2,'thread2',testTimes,total,target,size,results_dic,count)

# thread1.start()
# thread2.start()

# threads.append(thread1)
# threads.append(thread2)

# for thread in threads:
# 	thread.join()
#----------------------------------


#-----这段为主程序不使用多线程---------
for num in range(testTimes):
	values = generate(total= total, target= target)
	result = catch(values= values, target = target, size = size)
	add_to_dic(result= result, dic = results_dic)
#----------------------------------

results_dic = sorted(results_dic.items())


x_labels = [a[0] for a in results_dic]
fequency = [a[1] for a in results_dic]
time2 = time.time()

hist = pygal.Bar(x_label_rotation=-45, show_minor_x_labels=False)
hist.title = '一共%d数据，敏感数据%d个，抓取大小%d共%d次-耗时%.2f秒'%(total,target,size,testTimes,(time2-time1))
hist.x_title = '次'
hist.y_title = '频率'
hist.x_labels = x_labels
hist.add(title = 'A', values = fequency)

#hist.x_labels_major = x_labels[::10]
hist.title_font_size = 24
hist.label_font_size = 14
hist.major_label_font_size = 18

hist.render_to_file('visual.svg')

print("用时%.2f秒"%(time2-time1))
