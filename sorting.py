"""
MS practice
"""
list1=[3,5,2,7,9,0]
def bubble_sort(ls):
	i=0
	# times=0
	while i<len(ls):
		j=0
		while j<len(ls)-1:
			if ls[j]>ls[j+1]:
				temp=ls[j]
				ls[j]=ls[j+1]
				ls[j+1]=temp
			j+=1
			# times+=1
		i+=1
	return ls

def bubble_sort_improve(ls):
	i=0
	swap=1
	# times=0
	while i<len(ls) and swap==1:
		swap=0
		j=0
		while j<len(ls)-1:
			if ls[j]>ls[j+1]:
				temp=ls[j]
				ls[j]=ls[j+1]
				ls[j+1]=temp
				swap=1
			j+=1
			# times+=1
		i+=1
	return ls








	
