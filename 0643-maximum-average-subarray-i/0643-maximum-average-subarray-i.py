class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum=0
        w=sum(nums[:k])
        maximum=w

        for i in range(k,len(nums)):
            w=w+nums[i]-nums[i-k]
            if w> maximum:
                maximum=w

        answer=maximum/k

        return answer