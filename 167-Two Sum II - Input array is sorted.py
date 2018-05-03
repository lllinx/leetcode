"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
#method1: two pointer approach
def twoSum1(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r,s=0,len(numbers)-1,0
        while l<r:
            s=numbers[l]+numbers[r]
            if s==target:
                return [l+1,r+1]
            elif s<target:
                l+=1
            else:
                r-=1

#method2: binary search
def twoSum2(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            l,r=i+1,len(numbers)-1
            other=target-numbers[i]
            while l<=r:
                mid=l+(r-l)//2
                if other==numbers[mid]:
                    return [i+1,mid+1]
                elif other<numbers[mid]:
                    r-=1
                else:
                    l+=1


