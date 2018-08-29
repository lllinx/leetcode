"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

def groupAnagrams(strs):
	dic={}
	result=[]
	for str1 in strs:
		if "".join(sorted(str1)) not in dic:
			dic["".join(sorted(str1))]=[str1]
		else:
			dic["".join(sorted(str1))].append(str1)
	for v in dic.values():
		result.append(v)
	return result

