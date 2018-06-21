def avg_word(s):
	word=s.split(" ")
	word=[i for i in word if i!=""]
	total=0
	for i in word:
		total+=len(i)
	return total/len(word)

def valid_IP(ip):
	new_IP=ip.split(".")
	if len(new_IP)!=4:
		return False
	for i in new_IP:
		if int(i)<0 or int(i)>255 or (i[0]=="0" and len(i)>=2):
			return False
	return True

def friend_rel_count(l):
	dic={}
	for i in l:
		if len(i)==1:
				dic[i[0]]=0
		else:
			for j in i:
				if j not in dic:
					dic[j]=1
				else:
					dic[j]+=1
	return dic

