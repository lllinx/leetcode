"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:

Input: ["23:59","00:00"]
Output: 1

Note:

    The number of time points in the given list is at least 2 and won't exceed 20000.
    The input time is legal and ranges from 00:00 to 23:59.
"""

def findMinDifference(timepoints):
	time=[]
	for t in timepoints:
		t1=t.split(":")
		h=int(t1[0])
		m=int(t1[1])
		time.append(h*60+m)
	time=sorted(time)
	diff=time[1]-time[0]
	for i in range(1,len(time)):
		if time[i]-time[i-1]<diff:
			diff=time[i]-time[i-1]
	diff=min(diff,24*60-time[-1]+time[0])
	return diff




