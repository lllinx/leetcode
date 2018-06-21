"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""

class Interval:
	def __init__(self,s=0,e=0):
		self.start=s
		self.end=e

in1=Interval(1,3)
in2=Interval(2,6)
in3=Interval(8,10)
in4=Interval(15,18)
inter=[in1,in2,in3,in4]

def merge(intervals):
	out=[]
	for i in sorted(intervals, key=lambda x: x.start):
		if out and i.start<=out[-1].end:
			out[-1].end=max(out[-1].end,i.end)
		else:
			out.append(i)
	return out

