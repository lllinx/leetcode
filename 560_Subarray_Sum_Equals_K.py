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

def subarraySum3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    

