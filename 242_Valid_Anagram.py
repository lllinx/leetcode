"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s)!=len(t):
        return False
    dic1, dic2={}, {}
    for i in s:
        if i in dic1:
            dic1[i]+=1
        else:
            dic1[i]=1
    for j in t:
        if j in dic2:
            dic2[j]+=1
        else:
            dic2[j]=1
    for k,v in dic1.items():
        if k not in dic2.keys() or dic2[k]!=v:
            return False
    return True
            