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


"""find intersection of 2 list:ex, A = [1, 1, 1, 1] B =[4, 5, 8, 1, 1]
return [1,1]"""
A=[1, 1, 1, 1]
B=[4, 5, 8, 1, 1]

def inter(l1,l2):
	output=[]
	for i in l1:
		if i in l2:
			output.append(i)
			l2.remove(i)
	return output


