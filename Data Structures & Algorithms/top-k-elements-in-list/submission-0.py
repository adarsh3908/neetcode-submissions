class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        f =[[] for i in range(len(nums)+1)]
        for i in nums:
            a[i] = 1+ a.get(i,0)
        for i,c in a.items():
            f[c].append(i)
        res=[]
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
                if len(res) == k:
                    return res





        