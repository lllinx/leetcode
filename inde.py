""" Indeed practice
是一個list中, 找到某一個position, 讓左邊的值加起來與右邊的值相同
(position本身的值不列入計算)
"""

a=[1,2,3,3,6,8,9]
def find_point(x):
	for i in range(1,len(x)):
		if sum(x[:i])==x[i+1]:
			return i
b=[1,2,3,4,4,2]
def find_point2(x):
	for i in range(1,len(x)-1):
		if sum(x[:i])==sum(x[i+1:]):
			return i
