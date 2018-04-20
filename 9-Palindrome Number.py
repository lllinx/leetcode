"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x<10:
            return True
        else:
            s=[]
            new_x=x
            while new_x>0:
                s.append(new_x%10)
                new_x=new_x//10
            new_result=int(sum([s[i]*pow(10,len(s)-i-1) for i in range(len(s))]))
            return new_result==x

