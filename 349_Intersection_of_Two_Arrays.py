"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:

Each element in the result must be unique.
The result can be in any order.
"""

def intersection(nums1,nums2):
	dic, intersect={}, {}
	for i in nums1:
		if i not in dic:
			dic[i]=1
	for j in nums2:
		if j in dic:
			intersect[j]=1
	result=[j for j in intersect]
	return result

def intersection2(nums1,nums2):
	nums1.sort()
	nums2.sort()
	i,j=0,0
	dic={}
	while i<len(nums1) and j<len(nums2):
		if nums1[i]==nums2[j]:
			if nums1[i] not in dic:
				dic[nums1[i]]=1
			i+=1
			j+=1
		elif nums1[i]>nums2[j]:
			j+=1
		else:
			i+=1
	result=[k for k in dic]
	return result






