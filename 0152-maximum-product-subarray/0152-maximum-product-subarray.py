class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        current_max=nums[0]
        current_min=nums[0]
        answer=nums[0]

        for i in range(1,len(nums)):
            x=nums[i]

            temp_max=max(x,current_max*x,current_min*x)

            temp_min=min(x,current_max*x,current_min*x)

            current_max=temp_max
            current_min=temp_min
            answer=max(answer,current_max)

        return answer