"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

def findRepeatedDnaSequences(s):
	new={}
	repeated={}
	for i in range(len(s)-9):
		if s[i:i+10] in new:
			repeated[s[i:i+10]]=1
		else:
			new[s[i:i+10]]=1
	return list(repeated.keys())

