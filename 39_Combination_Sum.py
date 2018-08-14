"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

def combinationSum(candidates,target):
  candidates.sort()
  res=[]
  def dfs(candidates,remainder,res,temp,index):
    if remainder<0:
      return
    elif remainder==0:
      res.append(temp[:])
      return
    for i in range(index,len(candidates)):
      temp.append(candidates[i])
      dfs(candidates,remainder-candidates[i],res,temp,i)
      temp.pop()
    return res
  dfs(candidates,target,res,[],0)
  return res



		









