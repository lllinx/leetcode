def avg_word(s):
	word=s.split(" ")
	word=[i for i in word if i!=""]
	total=0
	for i in word:
		total+=len(i)
	return total/len(word)

def valid_IP(ip):
	new_IP=ip.split(".")
	if len(new_IP)!=4:
		return False
	for i in new_IP:
		if int(i)<0 or int(i)>255 or (i[0]=="0" and len(i)>=2):
			return False
	return True

def friend_rel_count(l):
	dic={}
	for i in l:
		if len(i)==1:
				dic[i[0]]=0
		else:
			for j in i:
				if j not in dic:
					dic[j]=1
				else:
					dic[j]+=1
	return dic

"""
Find common elements of two sorted arrays, try to optimize the space utility
a=[1,2,4,7,10,12,15]
b=[-1,2,3,8,10,13,15,17]
output=[2,10,15]
"""
def common_element(a,b):
	result=[]
	for i in a:
		low,high=0,len(b)-1
		while low<high:
			mid=(low+high)//2
			if i==b[mid]:
				result.append(i)
				break
			elif i<b[mid]:
				high=mid-1
			else:
				low=mid+1
	return result

def common_element2(a,b):
	index1,index2=0,0
	result=[]
	while index1<len(a) and index2<len(b):
		if a[index1]==b[index2]:
			result.append(a[index1])
			index1+=1
			index2+=1
		elif a[index1]>b[index2]:
			index2+=1
		else:
			index1+=1
	return result

print(common_element2([1,2,4,7],[-1,2,3,8]))


"""
Count distinct words in a sentence
"""
def count_distinct_word(s):
	result=[]
	s=s.split(" ")
	for i in s:
		if i not in result:
			result.append(i)
	return len(result)

print(count_distinct_word("wonderful summer time you are my sunshine sunshine summer time"))

"""
Find the distinct elements in an input integer list, order by its original order
"""
def distinct_list(l):
	if not l:
		return 
	result=[]
	for i in l:
		if result and i!=result[-1]:
			result.append(i)
		elif not result:
			result.append(i)
	return result

print(distinct_list([1,2,2,3,5,7,7,9]))


"""
flat list: giving [1,2,[3,4,[5,6]],7] ==> [1,2,3,4,5,6,7]
"""
def flatten(a):
	if type(a) is list:
		if len(a)==0:
			return []
		return flatten(a[0])+flatten(a[1:])
	else:
		return [a]

print(flatten([1,2,[3,4,[5,6]],7]))

"""
Count substr in string 
"""
def count_substr(string, sub):
	result=0
	for i in range(len(string)-len(sub)):
		if string[i:i+len(sub)]==sub:
			result+=1
	return result

print(count_substr("ababcool ab co","ab"))


def valid_parenthesis(s):
	stack=[]
	dic={")":"(","}":"{","]":"["}
	for i in s:
		if i in dic.values():
			stack.append(i)
		elif i in dic.keys():
			if not stack or dic[i]!=stack.pop():
				return False
	return stack==[]

def shortest_distance(words, word1, word2):
	distance=len(words)
	index1,index2=-1,-1
	for i in range(len(words)):
		if words[i]==word1:
			index1=i
		elif words[i]==word2:
			index2=i
		if index1!=-1 and index2!=-1:
			distance=min(distance,abs(index1-index2))
	return distance

"""
find closest distance of two same words in a string
"""
def shortest_distance_2(words):
	dic={}
	for i in range(len(words)):
		if i not in dic:
			dic[i]


"string substitution"

# def string_substi(s,s1):




"""
InputString = "babca", sortedString = "bca". Get the result = "bbcaa" 
(The characters in the result string should have the same order of the sortedString, 
and same counts of the InputString)
"""
def string_mute(s1,s2):
	result={}
	output=""
	for i in s1:
		if i not in result:
			result[i]=1
		else:
			result[i]+=1
	for j in s2:
		output+=j*result[j]
	return output
		
	

"""
int[] a = {1,0,0,2,0,3,......1,0,2,3}
int[] b = {1,1,0,0,0,1,......2,1,0,1}
1. Find the SUM(a * b) (a and b could have the different size)
2. How to optimize the arrays so it can get the SUM(a * b) faster
"""
def sum_ab(a,b):
	length=min(len(a),len(b))
	result=0
	for i in range(length):
		result+=a[i]*b[i]
	return result














