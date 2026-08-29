class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n

        # Prefix product
        left_product = 1

        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Suffix product
        right_product = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer