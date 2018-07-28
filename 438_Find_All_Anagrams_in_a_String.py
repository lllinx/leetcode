"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

def findAnagrams(s,p):
	dic={}
	for p1 in p:
		if p1 not in dic:
			dic[p1]=1
		else:
			dic[p1]+=1

	result=[]
	begin, end = 0, 0
	count=len(dic)

	while end<len(s):
		if s[end] in dic:
			dic[s[end]]-=1
			if dic[s[end]]==0:
				count-=1
		end+=1

		while count==0:
			if end-begin==len(p):
				result.append(begin)
			if s[begin] in dic:
				dic[s[begin]]+=1
				if dic[s[begin]]>0:
					count+=1
			begin+=1
	return result

	















