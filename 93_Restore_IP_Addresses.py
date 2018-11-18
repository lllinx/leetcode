"""

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

"""

def restoreIPaddress(s):
	def valid(s):
		if len(s)>3 or len(s)==0 or int(s)>255 or (len(s)>1 and s[0]=="0"):
			return False
		return True

	result=[]
	for i in range(1,min(4,len(s)-2)):
		for j in range(i+1,min(i+4,len(s)-1)):
			for k in range(j+1,min(j+4,len(s))):
				if valid(s[:i]) and valid(s[i:j]) and valid(s[j:k]) and valid(s[k:]):
					result.append(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])
	return result