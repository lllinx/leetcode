
"""
1. words average count. 比如"hello" -> 5, " hello wor " -> 4, "hello world t-the" -> 5 (t-the算一个词）
"""
def word_ave(x):
	new=x.split(" ")
	new1=[i for i in new if i]
	i,s=0,0
	for ele in new1:
		i,s=i+1,s+len(ele)
	return s/i
word_ave("hello")
word_ave(" hello wor ")
word_ave("hello world t-the")

"""
2. valid IP address. 不能用regex，做validation就好，用“.”分开，要有4部分，每部分都要是数字而且在0-255之间
"""
def IP(x):
	new=x.split(".")
	if len(new)!=4:
		return False
	else:
		test=[int(i)>0 and int(i)<255 for i in new]
		return all(test)
"""
3. friend relationship count. input (list of list): [[A, B], [B, C], [B, D], [E]], output (dict): {A:1, B: 3, C:1, D:1, E:0}
"""
def count(x):
	friend=[]
	[friend.extend(i) for i in x]
	result={}

	for i in friend:
		if i not in result:
			result[i]=1
		else:
			result[i]+=1
	return result

friend=[["A", "B"], ["B", "C"], ["B", "D"], ["E"]]
count(friend)



