"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
def subarraySum3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    dic={0:1}
    sums, count=0, 0
    for i in range(len(nums)):
        sums+=nums[i]
        if (sums-k) in dic.keys():
            count+=dic[sums-k]
        if sums in dic.keys():
            dic[sums]+=1
        else:
            dic[sums]=1
    return count

    



def subarraySum1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    result=0
    sums=[]
    sums.append(0)
    for i in range(0,len(nums)):
        sums.append(sums[-1]+nums[i])
    i=0
    while i<len(nums):
        j=i+1
        while j<=len(nums):
            if sums[j]-sums[i]==k:
                result+=1
            j+=1
        i+=1
    return result


def subarraySum2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    result=0
    i=0
    while i<len(nums):
        j=i
        sums=0
        while j<len(nums):
            sums+=nums[j]
            if sums==k:
                result+=1
            j+=1
        i+=1
    return result



    

