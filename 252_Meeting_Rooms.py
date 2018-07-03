"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: [[7,10],[2,4]]
Output: true
"""
class Interval:
	def __init__(self,s=0,e=0):
		self.start=s
		self.end=e

def canAttendMeetings(intervals):
	intervals.sort(key=lambda k:k.start)
	for i in range(1,len(intervals)):
		if intervals[i].start<intervals[i-1].end:
			return False
	return True

