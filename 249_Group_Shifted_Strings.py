"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

"""
def groupStrings(string):
	hashmap={}
	result=[]
	for str1 in string:
		offset=ord(str1[0])-ord("a")
		key=""
		for s in str1:
			char_ord=ord(s)-offset
			if char_ord<ord("a"):
				char=chr(ord(s)-offset+26)
			else:
				char=chr(ord(s)-offset)
			key+=char
		if key not in hashmap.keys():
			hashmap[key]=[str1]
		else:
			hashmap[key].append(str1)
	for v in hashmap.values():
		result.append(v)
	return result




