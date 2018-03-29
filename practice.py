"""word count based on a list"""
a=["how are you", "how are you 123", "132"]
b=[]
[b.extend(x.split(" ")) for x in a]

def count(x):
	output={}
	for i in x:
		if i not in output:
			output[i]=1
		else:
			output[i]+=1
	return output
