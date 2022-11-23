#Time_Complexity: O(n)
#Space_Complexity: O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0 #Initialize start as 0
        end = 0     #Initialize end as 0
        jumps = 0   #Initialize jumps as 0
        
        while end<len(nums)-1:  #Continue until end is less than len(nums)-1
            farthest = 0 #Initialize farthest as 0
            for i in range(start,end+1):    #Continue from start to the end+1
                farthest = max(farthest,i+nums[i])  #Change farthest with maximm between farthest and i+nums[i]

            jumps+=1    #Increment jumos by 1
            start = end+1   #Change start to end+1
            end = farthest  #Change end to farthest
        return jumps    #Return jumps which will give the number of jumps