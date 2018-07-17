"""
 Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

def intersect1(nums1,nums2):
	dic={}
	result=[]
	for i in nums1:
		if i not in dic:
			dic[i]=1
		else:
			dic[i]+=1
	for j in nums2:
		if j in dic and dic[j]>0:
			result.append(j)
			dic[j]-=1
	return result


def intersect2(nums1,nums2):
	nums1.sort()
	nums2.sort()
	i,j=0,0
	result=[]
	while i<len(nums1) and j<len(nums2):
		if nums1[i]==nums2[j]:
			result.append(nums1[i])
			i+=1
			j+=1
		elif nums1[i]>nums2[j]:
			j+=1
		else:
			i+=1
	return result



