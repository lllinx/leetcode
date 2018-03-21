# One string is an anagram of another if the second is simply a 
# rearrangement of the first. For example, 'heart' and 'earth' 
# are anagrams. The strings 'python' and 'typhon' are anagrams 
# as well. For the sake of simplicity, we will assume that the 
# two strings in question are of equal length and that they are 
# made up of symbols from the set of 26 lowercase alphabetic 
# characters.

#method1 
# O(n^2)
def check_off(s1,s2):
	p1=0
	still_ok=True
	s2_copy=list(s2)

	while p1<len(s1) and still_ok==True:
		p2=0
		in_s2=False
		while p2<len(s2_copy) and not in_s2:
			if s1[p1] == s2_copy[p2]:
				in_s2=True
			else:
				p2+=1

		if in_s2:
			s2_copy[p2]=None
		else:
			still_ok=False

		p1+=1

	return still_ok

# method2: sort and compare
# time complexity same as sorting algorithm
def sort_and_compare(s1,s2):
	s1_copy=list(s1)
	s2_copy=list(s2)
	s1_copy.sort()
	s2_copy.sort()

	Same=True
	p=0
	while p<len(s1) and Same:
		if s1_copy[p]==s2_copy[p]:
			p+=1
		else:
			Same=False
	return Same

#method3: count and compare
def count_and_compare(s1,s2):
	def count(s):
		dic={}
		for item in s:
			if item not in dic.keys():
				dic[item]=1
			else:
				dic[item]+=1
		return dic
	dic1, dic2 = count(s1), count(s2)
	if dic1==dic2:
		return True
	else:
		return False

# or method3: count_and_compare
# O(n)




