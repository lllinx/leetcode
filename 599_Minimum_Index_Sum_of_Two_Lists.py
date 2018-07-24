"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:

    The length of both lists will be in the range of [1, 1000].
    The length of strings in both lists will be in the range of [1, 30].
    The index is starting from 0 to the list length minus 1.
    No duplicates in both lists.
"""

def findRestaurant(list1,list2):
	dic={}
	for i in range(len(list1)):
		dic[list1[i]]=i

	min_sum=len(list1)+len(list2)-2
	result=[]
	for j in range(len(list2)):
		if list2[j] in dic:
			if j+dic[list2[j]]<min_sum:
				min_sum=j+dic[list2[j]]
				result=[list2[j]]
			elif j+dic[list2[j]]==min_sum:
				result.append(list2[j])
	return result





