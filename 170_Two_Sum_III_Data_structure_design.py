"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false

Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""
class TwoSum:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.num={}

	def add(self,number):
		"""
		Add the number to an internal data structure..
		:type number: int
		:rtype: void
		"""
		if number in self.num:
			self.num[number]+=1
		else:
			self.num[number]=1


	def find(self,value):
		"""
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
		for i in self.num.keys():
			if value-i in self.num.keys() and (value-i!=i or self.num[i]>1):
				return True
		return False

