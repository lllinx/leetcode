"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""
Class WordDictionary:
	def __init__(self):
		self.dic=collections.defaultdict(list)

	def addword(self,word):
		if word:
			self.dic[len(word)].append(word)

	def searchword(self,word):
		if not word:
			return False
		elif "." not in word:
			return word in self.dic[len(word)]
		else:
			for v in self.dic[len(word)]:
				for i,ch in enumerate(word):
					if v[i]!=ch and ch!=".":
						break
				else:
					return True
		return False

		







