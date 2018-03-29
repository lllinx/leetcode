"""The meaning of the strings are 'activity, start time, end time'"""

activity= ['running,0800,1000', 'swimming,1000,1100', 'eating,1100,1200','running,1115,1330']

#Write a function to output all the unique activities in the list#
def unique(x):
	return set([i.split(",")[0] for i in x])


#Write a function to calculate the duration of each activity in minutes#
def duration(x):
	new_list=[i.split(",") for i in x]
	result=[]
	for i in range(len(new_list)):
		element=new_list[i]
		result.append([element[0],(int(element[2][:2])-int(element[1][:2]))*60 + (int(element[2][2:])-int(element[1][2:]))])
	return result

# Write a function to merge all the time intervals in the list that have overlaps, leave the non-overlapping intervals alone, and finally output all non-overlapping time intervals after merging those that overlap. O(N^2) solution not acceptable.#
time=[x.split(",")[1:] for x in activity]
new_time=[]
[new_time.append([int(x[0]),int(x[1])]) for x in time]
def interval(x):
	result_overlap=[]
	result_interval=[]
	for i in range(len(x)-1):
		if i==1:
			if x[i][1]>x[i+1][0]:
				x[i].append(True)
			else:
				x[i].append(False)
		elif i>1 and i<len(x)-1:
			if x[i][1]>x[i+1][0] or x[i-1][1]>x[i][0]:
				x[i].append(True)
			else:
				x[i].append(False)
		elif i==len(x)-1:
			if x[i-1][1]>x[i][0]:
				x[i].append(True)
			else:
				x[i].append(False)
	return [i for i in x if i[2]==False]








