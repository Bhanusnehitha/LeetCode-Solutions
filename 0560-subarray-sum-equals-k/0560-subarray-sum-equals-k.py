class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = {0: 1}

        current_sum = 0
        count = 0

        for num in nums:

            current_sum += num

            needed = current_sum - k

            if needed in prefix:
                count += prefix[needed]

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

        return count