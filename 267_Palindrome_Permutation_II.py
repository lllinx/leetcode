"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]

Example 2:

Input: "abc"
Output: []

"""

def generatePalindromes(s):
	dic={}
	for s1 in s:
		if s1 not in dic:
			dic[s1]=1
		else:
			dic[s1]+=1
	sum_odd=0
	middle=""
	half=""
	for k,v in dic.items():
		if v%2==1:
			sum_odd+=1
			if sum_odd>1:
				return []
			middle=k
		half+=k*(v//2)
	res=[]
	used=[False for _ in half]
	def dfs(s,temp,res):
		if len(temp)==len(s):
			res.append(temp+middle+temp[::-1])
			return
		for i in range(len(s)):
			if used[i]:
				continue
			elif i>0 and s[i-1]==s[i] and not used[i-1]:
				continue
			temp+=s[i]
			used[i]=True
			dfs(s,temp,res)
			temp=temp[:-1]
			used[i]=False
		return res
	dfs(half,"",res)
	return res




	