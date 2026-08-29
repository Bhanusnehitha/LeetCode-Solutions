class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder = {0: -1}
        current_sum = 0

        for i in range(len(nums)):

            current_sum += nums[i]

            if k != 0:
                rem = current_sum % k
            else:
                rem = current_sum

            if rem in remainder:

                if i - remainder[rem] >= 2:
                    return True

            else:
                remainder[rem] = i

        return False