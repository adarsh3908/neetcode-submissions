class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        a = sorted(set(nums))
        count = 1
        ans = 1
        for i in range(len(a)-1):
            if a[i+1]-a[i] == 1:
                count +=1
            else:
                count = 1
            ans = max(count,ans)    
        return ans        