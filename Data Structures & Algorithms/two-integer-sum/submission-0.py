class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a ={}
        for  i,j in enumerate(nums):
            diff = target - j
            if diff in a:
                return [a[diff],i]
            a[j]  = i
        return       