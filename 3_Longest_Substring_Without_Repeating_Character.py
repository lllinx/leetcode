"""3. Longest Substring Without Repeating Characters
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence 
and not a substring.
"""
# brute force time O(N^3) space O(1)
def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	length=len(s)
	substring=[]
	i=0
	if length<=1:
		return length
	while i<length:
		string=s[i]
		j=i+1
		repeat=False
		while j<length and repeat==False:
			if s[j] not in string:
				string += s[j]
				j += 1
			else:
				repeat=True
		substring.append(string) 
		i += 1
	max_sub_len=max([len(i) for i in substring])
	return max_sub_len

# slicing window time O(n), space O(n)
def lengthOfLongestSubstring2(s):
	"""
	:type s: str
	:rtype: int
	"""
	dic={}
	result,i,j=0,0,0
	while i<len(s) and j<len(s):
		if s[j] not in dic:
			dic[s[j]]=1
			j+=1
			result=max(result,j-i)
		else:
			del dic[s[i]]
			i+=1
	return result







